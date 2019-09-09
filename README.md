# Gladiator-Royale

Project Completed December 2018
### Gladiator

The gladiator consists of name (string), age (int), birthplace (string), and health (int 0-100). The data is stored in a json file in the following format:
[
        {name: ‘ceasar’, age: 56, birthplace: ‘Rome’, health: 50}
...
]
Outcome rewards gladiators between ages 20-40, previous wins, health and random bonus

### Audience

The audience class observes the Gladiators as they go through the gladiatorial games, giving cheers, boos, or gasps as events occur in each match. Audience contains 100 audience objects that register as observers of the gladiator. The gladiator then ‘notifies’ the audience whenever an event occurs. There are 3 possible event types:
* The gladiator is harmed (loses health)
* The gladiator wins a match
* The gladiator loses a match

### Response

There are 3 audience member response strategies which will determine how different audience members respond to an event. For example, a negative response type would produce the following results:
* The gladiator is harmed (loses health) produces cheers
* The gladiator completes a task produces boos
* The gladiator fails a task produces cheers

Another response type, for example positive:
* The gladiator is harmed (loses health) produces boos
* The gladiator completes a task produces cheers
* The gladiator fails a task produces gasps

The response strategies are stored in their own class. Each audience member object is randomly assigned a response strategy. Each audience member randomly chooses one of the gladiators during the match to observe and respond to. The response strategy for each audience member is updated with a new response strategy for each match.


### Arena
The Arena class holds all the audience members, gladiators, and battle logic.

Gladiators will be put into the arena and compete in battle. Gladiators are stored in a queue logic will be to retrieve the next two gladiators from the pool of gladiators and have them battle until one reaches zero health. Then the audience will decide if the loser should have another chance with a thumbs up or thumbs down vote.

Each audience member will choose thumbs up or thumbs down to allow an "Encore" match to occur. Votes are taken at random and passed if more than half vote in-favor. Otherwise, the gladiator will be placed back in the pool of gladiators and live to fight another round. Encore matches will stop when the audience votes against it. 