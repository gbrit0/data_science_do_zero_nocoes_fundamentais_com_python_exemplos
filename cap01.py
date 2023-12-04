users = [ # data dump em que cada user é representado por um dict com seu id e name
    {"id":0, "name": "Hero"},
    {"id":1, "name": "Dunn"},
    {"id":2, "name": "Sue"},
    {"id":3, "name": "Chi"},
    {"id":4, "name": "Thor"},
    {"id":5, "name": "Clive"},
    {"id":6, "name": "Hicks"},
    {"id":7, "name": "Devin"},
    {"id":8, "name": "Kate"},
    {"id":9, "name": "Klein"},
]

friendships_pairs = [ # pares de id's representando as conexões, amizades.
    (0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)
]

# inicializando o dict(dicionário) com uma lista vazia para cada id de usuário
friendships = {
    user["id"]: [] for user in users
}
# loop pelos pares de amigo para preencher friednships:
for i, j in friendships_pairs:
    friendships[i].append(j) # Adiciona j como amigo de i
    friendships[j].append(i) # Adiciona i como amigo de j

# print(friendships)
def number_of_friends(user):
    """Quantos amigos tem o _user_?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)

# print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users # conexões médias

# print(avg_connections)

# Criar uma lista (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], # ordena a lista decrescentemente pela quantidade de conexões
                       reverse=True)

from collections import Counter # não é carregado por padrão

def friends_of_friends(user): # contagem de amigos em comum do user. Retorna o id do não amigo e a contagem de conexões em comum
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]    # Para cada amigo meu
        for foaf_id in friendships[friend_id]    # encontre os amigos deles
        if foaf_id != user_id                    # que não sejam eu
        and foaf_id not in friendships[user_id]  # e não sejam meus amigos
    )

print(friends_of_friends(users[3])) # Counter({0: 2, 5: 1})