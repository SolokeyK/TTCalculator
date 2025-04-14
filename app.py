from flask import Flask, render_template, request
import webbrowser
import TT 
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    origin_traits = [
        'Anima Squad', 'BoomBot', 'Cypher', 'Divinicorp', 'Exotech',
        'Golden Ox', 'Street Demon', 'Syndicate'
    ]
    class_traits = [
        'Bastion', 'Bruiser', 'Dynamo', 'Executioner', 'Marksman',
        'Rapidfire', 'Slayer', 'Strategist', 'Techie', 'Vanguard'
    ]
    one_cost_champs = sorted([champ for champ in TT.champ_dict if TT.champ_dict[champ]['cost'] == 1])
    two_cost_champs = sorted([champ for champ in TT.champ_dict if TT.champ_dict[champ]['cost'] == 2])
    three_cost_champs = sorted([champ for champ in TT.champ_dict if TT.champ_dict[champ]['cost'] == 3])
    four_cost_champs = sorted([champ for champ in TT.champ_dict if TT.champ_dict[champ]['cost'] == 4])

    if request.method == 'POST':
        try:
            maxPop = int(request.form['maxPop'])
            emblem_dict = {}
            for trait in origin_traits + class_traits:
                emblem_count = int(request.form.get(f'emblem_{trait}', 0))
                if emblem_count > 0:
                    emblem_dict[trait] = emblem_count
            hadChamp = request.form['hadChamp'].split(',') if request.form['hadChamp'] else []
            result = TT.TT_calculator(
                TT.champ_dict,
                TT.lmt_dict,
                maxPop,
                threshold=3,
                emblem_dict=emblem_dict if emblem_dict else None,
                incPop=0,
                hadChamp=hadChamp if hadChamp else None
            )[:5]
            extra_info = []
            if maxPop != 7:
                extra_info.append(f"with {maxPop} population")
            if emblem_dict:
                emblems_str = ", ".join([f"{count} * {trait} emblem" for trait, count in emblem_dict.items()])
                extra_info.append(emblems_str)
            if hadChamp:
                champs_str = ", ".join(hadChamp)
                extra_info.append(f"already have {champs_str}")
            extra_info_str = ", ".join(extra_info) if extra_info else ""
            return render_template(
                'index.html',
                result=result,
                extra_info=extra_info_str,
                origin_traits=origin_traits,
                class_traits=class_traits,
                one_cost_champs=one_cost_champs,
                two_cost_champs=two_cost_champs,
                three_cost_champs=three_cost_champs,
                four_cost_champs=four_cost_champs,
                champ_dict=TT.champ_dict
            )
        except Exception as e:
            logger.error(f"Error in POST request: {str(e)}", exc_info=True)
            return "An error occurred during calculation. Check the server logs for details.", 500

    return render_template(
        'index.html',
        result=[],
        extra_info="",
        origin_traits=origin_traits,
        class_traits=class_traits,
        one_cost_champs=one_cost_champs,
        two_cost_champs=two_cost_champs,
        three_cost_champs=three_cost_champs,
        four_cost_champs=four_cost_champs,
        champ_dict=TT.champ_dict
    )

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """Shutdown the Flask server and terminate the process."""
    os._exit(0) 
    return "Server shutting down..."

if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=False)