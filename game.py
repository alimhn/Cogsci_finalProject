import random

maze = {
    'First': {
        'sensory input':['You have been wandering in the forest for days now, you see a wooden house hidden between woods with an apple tree with lots of apple on it. The house looks spooky to you'],
        'actions': {
            'Take an apple': {
                # 'success': 'You gather your courage and enter the dark, scary jungle.',
                # 'failure': 'You decide to stay hungry, hoping to find food elsewhere.',
                'next_room': 'Second',
                'required_sensory input': []
            },
            'Knock on the door to ask for an apple': {
                # 'success': 'You choose to stay hungry and continue your search for food.',
                # 'failure': 'Your hunger overwhelms you, and you decide to take the risk and enter the jungle.',
                'next_room': 'Third',
                'required_sensory input': []
            },
            'Go around the house': {
                # 'success': 'You choose to stay hungry and continue your search for food.',
                # 'failure': 'Your hunger overwhelms you, and you decide to take the risk and enter the jungle.',
                'next_room': 'Final',
                'required_sensory input': []
            }
        }
    },
    'Second': {
        'sensory input': ['You feel like being watched.'],
        'actions': {
            'Fill your pockets with apple': {
                # 'success': 'You knock the door, and a scary witch opens it, inviting you inside.',
                # 'failure': 'You decide not to knock the door and look for food elsewhere.',
                'next_room': 'Second',
                'required_sensory input': []
            },
            'Sit under apple tree while eaten apple': {
                # 'success': 'You knock the door, and a scary witch opens it, inviting you inside.',
                # 'failure': 'You decide not to knock the door and look for food elsewhere.',
                'next_room': 'Success',
                'required_sensory input': []
            },
            'Check house': {
                # 'success': 'You knock the door, and a scary witch opens it, inviting you inside.',
                # 'failure': 'You decide not to knock the door and look for food elsewhere.',
                'next_room': 'Final',
                'required_sensory input': []
            }

        }
    },
    'Third': {
        'sensory input': ['Nobody answers the door.'],
        'actions': {
            'Go near apple tree': {
                # 'success': 'You eat the apple and satisfy your hunger!',
                # 'failure': 'You decide not to eat the apple and keep searching for food.',
                'next_room': 'Second',
                'required_sensory input': []
            },
            'Check windows': {
                # 'success': 'You eat the apple and satisfy your hunger!',
                # 'failure': 'You decide not to eat the apple and keep searching for food.',
                'next_room': 'Final',
                'required_sensory input': []
            },
            'Wander around the house': {
                # 'success': 'You eat the apple and satisfy your hunger!',
                # 'failure': 'You decide not to eat the apple and keep searching for food.',
                'next_room': 'Final',
                'required_sensory input': []
            }
        }
    },
    'Final': {
        'sensory input': ['You see a half open back door.'],
        'actions': {
            'Vocal call, calmly': {
                # 'success': 'You eat the apple and satisfy your hunger!',
                # 'failure': 'You decide not to eat the apple and keep searching for food.',
                'next_room': 'Third',
                'required_sensory input': []
            },
            'Check backyard and try to find a path': {
                # 'success': 'You eat the apple and satisfy your hunger!',
                # 'failure': 'You decide not to eat the apple and keep searching for food.',
                'next_room': 'Final',
                'required_sensory input': []
            },
            'Forget about apple, walk away, house looks spooky': {
                # 'success': 'You eat the apple and satisfy your hunger!',
                # 'failure': 'You decide not to eat the apple and keep searching for food.',
                'next_room': 'Failure',
                'required_sensory input': []
            }
        }
    },
    'Success, you were able to feed yourself': {
        'sensory input': [],
        'actions': {}
    },
    'Failiure, you remained hungry': {
        'sensory input': [],
        'actions': {}
    }
}

current_room = 'First'
score = 0

while current_room:
    if current_room == 'Success':
        print("\n*****************************")
        print("Congratulations! You could feed yourself.")
        print("*****************************\n")
        break
    elif current_room == 'Failure':
        print("\n*****************************")
        print("Failure, you remained hungry.")
        print("*****************************\n")
        break
    else:
        print("\n-------------------------------")
        print(f"You are in {current_room}.")
        print("-------------------------------\n")
        print("sensory input:\n\n", maze[current_room]['sensory input'])
        print("\nActions:\n")
        for i, action in enumerate(maze[current_room]['actions'], start=1):
            print(f"{i}. {action}")

        valid_input = False
        while not valid_input:
            choice = input("Enter your action number: ")

            if choice.isdigit() and 1 <= int(choice) <= len(maze[current_room]['actions']):
                valid_input = True
            else:
                print("Invalid action number. Try again.")

        actions = list(maze[current_room]['actions'].keys())
        chosen_action = actions[int(choice) - 1]
        consequences = maze[current_room]['actions'][chosen_action]

        if all(obj in maze[current_room]['sensory input'] for obj in consequences['required_sensory input']):
            # print(consequences['success'])
            # score += 1
            current_room = consequences['next_room']
        # else:
        #     print(consequences['failure'])
        #     score -= 1

# print(f"Congratulations! You reached the exit. Your score is {score}.")
