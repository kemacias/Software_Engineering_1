


```mermaid
classDiagram
    Effects <|-- poison
    Effects <|-- Regen
    Item <|-- Key
    Item <|-- Weapon
    Sword <|-- Weapon
    Bow <|-- Weapon
    Consumable <|-- item
    Poison <|-- Consumable
    Entity <|-- Describable
    Creature <|-- Entity
    Player <|-- Creature
    Monster <|-- Creature
    Gobin <|-- Flamable
    Goblin <|-- Monster
    Skeleton <|-- Monster
```
