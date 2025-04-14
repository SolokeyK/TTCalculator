import pickle
import os
from collections import OrderedDict
import copy

CACHE_FILE = 'cache.pkl'

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'rb') as f:
        cache = pickle.load(f)
else:
    cache = {}

champ_dict = {
    'Brand': {'cost': 4, 'traits': ['Street Demon', 'Techie']},
    'Darius': {'cost': 2, 'traits': ['Syndicate', 'Bruiser']},
    'Dr. Mundo': {'cost': 1, 'traits': ['Street Demon', 'Bruiser', 'Slayer']},
    'Elise': {'cost': 3, 'traits': ['Nitro', 'Dynamo']},
    'Fiddlesticks': {'cost': 3, 'traits': ['BoomBot', 'Techie']},
    'Galio': {'cost': 3, 'traits': ['Cypher', 'Bastion']},
    'LeBlanc': {'cost': 2, 'traits': ['Cypher', 'Strategist']},
    'Miss Fortune': {'cost': 4, 'traits': ['Syndicate', 'Dynamo']},
    'Morgana': {'cost': 1, 'traits': ['Divinicorp', 'Dynamo']},
    'Neeko': {'cost': 4, 'traits': ['Street Demon', 'Strategist']},
    'Renekton': {'cost': 5, 'traits': ['Divinicorp', 'Bastion']},
    'Rengar': {'cost': 3, 'traits': ['Street Demon', 'Executioner']},
    'Samira': {'cost': 5, 'traits': ['Street Demon', 'A.M.P.']},
    'Senna': {'cost': 3, 'traits': ['Divinicorp', 'Slayer']},
    'Shaco': {'cost': 1, 'traits': ['Syndicate', 'Slayer']},
    'Twisted Fate': {'cost': 2, 'traits': ['Syndicate', 'Rapidfire']},
    'Varus': {'cost': 3, 'traits': ['Exotech', 'Executioner']},
    'Veigar': {'cost': 2, 'traits': ['Cyberboss', 'Techie']},
    'Vex': {'cost': 4, 'traits': ['Divinicorp', 'Executioner']},
    'Zed': {'cost': 4, 'traits': ['Cypher', 'Slayer']},
    'Zeri': {'cost': 4, 'traits': ['Exotech', 'Rapidfire']},
    'Zyra': {'cost': 1, 'traits': ['Street Demon', 'Techie']},
    'Braum': {'cost': 3, 'traits': ['Syndicate', 'Vanguard']},
    'Nidalee': {'cost': 1, 'traits': ['Nitro', 'A.M.P.']},
    'Shyvana': {'cost': 2, 'traits': ['Nitro', 'Bastion', 'Techie']},
    'Kindred': {'cost': 1, 'traits': ['Nitro', 'Rapidfire', 'Marksman']},
    'Yuumi': {'cost': 3, 'traits': ['Anima Squad', 'A.M.P.', 'Strategist']},
    'Illaoi': {'cost': 2, 'traits': ['Anima Squad', 'Bastion']},
    'Seraphine': {'cost': 1, 'traits': ['Anima Squad', 'Techie']},
    'Xayah': {'cost': 4, 'traits': ['Anima Squad', 'Marksman']},
    'Jhin': {'cost': 2, 'traits': ['Exotech', 'Marksman', 'Dynamo']},
    'Naafiri': {'cost': 2, 'traits': ['Exotech', 'A.M.P.']},
    'Gragas': {'cost': 3, 'traits': ['Divinicorp', 'Bruiser']},
    "Kog'Maw": {'cost': 1, 'traits': ['BoomBot', 'Rapidfire']},
    'Skarner': {'cost': 2, 'traits': ['BoomBot', 'Vanguard']},
    'Jax': {'cost': 1, 'traits': ['Exotech', 'Bastion']},
    'Kobuko': {'cost': 5, 'traits': ['Cyberboss', 'Bruiser']},
    'Sejuani': {'cost': 4, 'traits': ['Exotech', 'Bastion']},
    'Poppy': {'cost': 1, 'traits': ['Cyberboss', 'Bastion']},
    'Ziggs': {'cost': 4, 'traits': ['Cyberboss', 'Strategist']},
    "Cho'Gath": {'cost': 4, 'traits': ['BoomBot', 'Bruiser']},
    'Urgot': {'cost': 5, 'traits': ['BoomBot', 'Executioner']},
    'Sylas': {'cost': 1, 'traits': ['Anima Squad', 'Vanguard']},
    'Aurora': {'cost': 5, 'traits': ['Anima Squad', 'Dynamo']},
    'Vayne': {'cost': 2, 'traits': ['Anima Squad', 'Slayer']},
    'Leona': {'cost': 4, 'traits': ['Anima Squad', 'Vanguard']},
    'Vi': {'cost': 1, 'traits': ['Cypher', 'Vanguard']},
    'Mordekaiser': {'cost': 3, 'traits': ['Exotech', 'Bruiser', 'Techie']},
    'Alistar': {'cost': 1, 'traits': ['Golden Ox', 'Bruiser']},
    'Viego': {'cost': 5, 'traits': ['Golden Ox', 'Techie']},
    'Jarvan IV': {'cost': 3, 'traits': ['Golden Ox', 'Vanguard', 'Slayer']},
    'Graves': {'cost': 2, 'traits': ['Golden Ox', 'Executioner']},
    'Annie': {'cost': 4, 'traits': ['Golden Ox', 'A.M.P.']},
    'Rhaast': {'cost': 2, 'traits': ['Divinicorp', 'Vanguard']},
    'Draven': {'cost': 3, 'traits': ['Cypher', 'Rapidfire']},
    'Jinx': {'cost': 3, 'traits': ['Street Demon', 'Marksman']},
    'Ekko': {'cost': 2, 'traits': ['Street Demon', 'Strategist']},
    'Aphelios': {'cost': 4, 'traits': ['Golden Ox', 'Marksman']},
}

lmt_dict = {
    'Street Demon': 3,
    'Techie': 2,
    'Syndicate': 3,
    'Bruiser': 2,
    'Slayer': 2,
    'Nitro': 3,
    'Dynamo': 2,
    'BoomBot': 2,
    'Cypher': 3,
    'Bastion': 2,
    'Strategist': 2,
    'Divinicorp': 1,
    'Executioner': 2,
    'A.M.P.': 2,
    'Rapidfire': 2,
    'Exotech': 3,
    'Cyberboss': 2,
    'Vanguard': 2,
    'Marksman': 2,
    'Anima Squad': 3,
    'Golden Ox': 2,
}

def TT_calculator(champ_dict, lmt_dict, maxPop, threshold=3, emblem_dict=None, incPop=0, hadChamp=None):
    """
    Calculate team compositions with caching.
    
    Args:
        champ_dict (dict): Dictionary of champions and their traits/costs.
        lmt_dict (dict): Dictionary of trait activation thresholds.
        maxPop (int): Maximum population size.
        threshold (int): Maximum cost threshold for champions (default: 3).
        emblem_dict (dict): Optional dictionary of emblem counts per trait.
        incPop (int): Incremental population adjustment (default: 0).
        hadChamp (list): List of champions already selected (default: None).
    
    Returns:
        list: Sorted list of solutions (champion selections, traits, cost).
    """
    key = (
        maxPop,
        frozenset(emblem_dict.items()) if emblem_dict else None,
        tuple(hadChamp) if hadChamp else None,
        incPop
    )
    
    if key in cache:
        return cache[key]

    if hadChamp is None:
        hadChamp = []

    effective_maxPop = maxPop + incPop

    champ_dict_copy = copy.deepcopy(champ_dict)
    for champ in hadChamp:
        if champ in champ_dict_copy:
            champ_dict_copy[champ]['cost'] = 0

    lmt_dict_copy = copy.deepcopy(lmt_dict)
    if emblem_dict:
        for trait, count in emblem_dict.items():
            if trait in lmt_dict_copy:
                lmt_dict_copy[trait] -= count

    eligible_champs = [champ for champ in champ_dict_copy if champ_dict_copy[champ]['cost'] <= threshold]
    all_solutions = []

    def dfs(start, current_selection, current_lmt_dict, current_cost):
        """Depth-first search to find valid team compositions."""
        if len(current_selection) == effective_maxPop:
            current_activated = sum(1 for count in current_lmt_dict.values() if count <= 0)
            if current_activated >= 8:
                trait_contributions = calculate_trait_contributions(current_selection)
                sorted_trait_list = sort_trait_list(trait_contributions, lmt_dict)
                all_solutions.append((current_selection[:], sorted_trait_list, current_cost))
            return

        for i in range(start, len(eligible_champs)):
            champ = eligible_champs[i]
            if champ not in current_selection:
                new_lmt_dict = current_lmt_dict.copy()
                for trait in champ_dict_copy[champ]['traits']:
                    if trait in new_lmt_dict:
                        new_lmt_dict[trait] -= 1
                new_cost = current_cost + (0 if champ in hadChamp else champ_dict[champ]['cost'])
                dfs(i + 1, current_selection + [champ], new_lmt_dict, new_cost)

    def calculate_trait_contributions(selection):
        """Calculate how many times each trait is contributed by the selection."""
        trait_contributions = {trait: 0 for trait in lmt_dict}
        for champ in selection:
            for trait in champ_dict[champ]['traits']:
                if trait in trait_contributions:
                    trait_contributions[trait] += 1
        if emblem_dict:
            for trait, count in emblem_dict.items():
                if trait in trait_contributions:
                    trait_contributions[trait] += count
        return trait_contributions

    def sort_trait_list(trait_contributions, lmt_dict):
        """Sort traits based on activation and threshold."""
        trait_list = [
            (trait, (trait_contributions[trait], lmt_dict[trait]))
            for trait in lmt_dict
        ]
        return sorted(
            trait_list,
            key=lambda item: (item[1][0] < item[1][1], -item[1][1], item[0])
        )

    dfs(0, [], lmt_dict_copy, 0)
    sorted_solutions = sorted(all_solutions, key=lambda x: x[2])

    cache[key] = sorted_solutions
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)

    return sorted_solutions