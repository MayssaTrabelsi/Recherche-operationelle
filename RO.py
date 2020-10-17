#!/usr/bin/env python
# coding: utf-8

# # LE MYSTÉRIEUX TRÉSOR DU PRINCE SOLTYKOFF

# In[12]:


#Nous allons créer un dictionnaire pour représenter le graphe
graph = {

'Départ':{'Marché':4,
          'Foret':1},
'Foret':{'Marché':2,
          'Capital':7},
'Marché':{'Col':5,
          'Capital':3},
'Col':{'Refuge':3},
'Capital':{'Refuge':4,
           'Palais':10},
'Refuge':{'Epee':20,
          'Grotte':32,
          'Palais':5},
'Palais':{'Carte':6},
'Carte':{'Tresor':30,
         'Epee':7},
'Epee':{'Grotte':8, 
        'Tresor':18},
'Grotte':{'Tresor':9},
'Tresor':{'Grotte':1}
}


# In[13]:


graph


# In[14]:


def dijkstra(graph,start,goal):

    shortest_distance = {} #dictionnaire pour enregistrer le poids pour atteindre le nœud.
    #Nous mettrons constamment à jour ce dictionnaire au fur et à mesure que nous avancerons dans le graphe.
    track_predecessor = {} #dictionnaire pour garder une trace du chemin qui a conduit à ce nœud
    unseenNodes = graph #pour parcourir tous les nœuds
    infinity = 5000 #l'infini peut être considéré comme un très grand nombre
    track_path = [] #dictionnaire pour enregistrer pendant que nous remontons notre voyage



# =============================================================================
# Initialement, nous voulons attribuer 0 comme poids à atteindre au nœud source et l'infini comme poids à tous les autres nœuds
# =============================================================================

    for node in unseenNodes:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0

# =============================================================================
# La boucle continuera de fonctionner jusqu'à ce que nous ayons complètement épuisé le graphe, 
#jusqu'à ce que nous ayons vu tous les nœuds
# =============================================================================
# =============================================================================
# Pour parcourir le graphique, nous devons à chaque fois déterminer le min_distance_node.
# =============================================================================

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

# =============================================================================
# A partir du nœud minimum, quels sont nos chemins possibles
# =============================================================================

        path_options = graph[min_distance_node].items()


# =============================================================================
# Nous devons calculer le poids à chaque fois pour chaque chemin que nous empruntons et le mettre à jour 
#uniquement s'il est inférieur au poids existant
# =============================================================================

        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:

                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]

                track_predecessor[child_node] = min_distance_node

# =============================================================================
# Nous voulons faire ressortir les nœuds que nous venons de visiter afin de ne plus les parcourir.
# =============================================================================
        unseenNodes.pop(min_distance_node)



# =============================================================================
# Une fois que nous avons atteint le nœud de destination, nous voulons remonter notre chemin
#et calculer le poids total accumulé
# =============================================================================

    currentNode = goal

    while currentNode != start:

        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    track_path.insert(0,start)


# =============================================================================
# Si le poids est infini, le nœud n'a pas été atteint.
# =============================================================================
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(track_path))


dijkstra(graph, 'Départ', 'Tresor')


# # MERCI POUR VOTRE ATTENTION!
