import json
import os
import sys
# Manually adjust the sys.path at the top of the script
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.append(project_root)

# Now import the helper function
from utils.path_helpers import add_project_root_to_sys_path
from utils.create_prompt import create_prompt

# Use the helper function to ensure the project root is in sys.path
add_project_root_to_sys_path()

MOCK_JSON_OBJECT = {
    "Factions": {
        "Boomers": {
            "Background": [
                " from Lake Mead . [16] [17] At some point, the NCR attempted to shut off the Boomers' water supply. The Boomers' response was to shell sections of the NCR's water pipeline in eastern New Vegas, which led to the NCR quickly retracting their decision and restoring the water flow. In the months that followed, no one else has tried to approach the Boomers, a status quo that they greatly prefer. [Non-game 2]",
                ", that did not deter the Boomers. Equipped with Geiger counters , they assessed Nellis and learned that much of the radioactivity had decayed to safe levels. [6] The Boomers moved in and restored the base to working order. [7] [3] Although Nellis was well fortified, the Boomers identified several security issues. In keeping with their social customs, they decided to patch them with extreme firepower. A large expedition was formed, which retrieved howitzers and the appropriate ammunition stockpiles from Area 2 . The expedition lasted weeks, but was ultimately successful and marked the last time that Boomers set foot outside Nellis. [8] Anyone coming within a mile of the base is fired upon and destroyed with extreme prejudice. [9] The Boomers lived and prospered in Nellis. However, indefinite isolation was not their goal. When Loyal , one of the tribe's Elders, found a file on the crashed B-29 bomber in Lake Mead , the Boomers' efforts became focused. [10] Recovering and repairing the bomber became their destiny. [11] To that end, the Boomers reactivated the virtual reality simulators used for pilot training before the war, using them to develop and refine their flying skills to \"fly the open skies in armored safety, raining high-explosive ordnance upon ignorant savages\", as the Keeper of the Story puts it. [3] [12] Of course",
                "to high radiation levels. [3] Wastelanders and animals learned to avoid it by habit, leaving it in relatively good condition. [5] However, that did not deter the Boomers. Equipped with Geiger counters , they assessed Nellis and learned that much of the radioactivity had decayed to safe levels. [6] The Boomers moved in and restored the base to working order. [7] [3] Although Nellis was well fortified, the Boomers identified several security issues. In keeping with their social customs, they decided to patch them with extreme firepower. A large expedition was formed, which retrieved howitzers and the appropriate ammunition stockpiles from Area 2 . The expedition lasted weeks, but was ultimately successful and marked the last time that Boomers set foot outside Nellis. [8] Anyone coming within a mile of the base is fired upon and destroyed with extreme prejudice. [9] The Boomers lived and prospered in Nellis. However, indefinite isolation was not their goal. When Loyal , one of the tribe's Elders, found a file on the crashed B-29 bomber in Lake Mead , the Boomers' efforts became focused. [10] Recovering and repairing the bomber became their destiny. [11] To that end, the Boomers reactivated the virtual reality simulators"
            ],
            "Society": [
                " the Master-at-Arms is responsible for the security of the Nellis homeland, from the coordination of its defenses to the training and fitness of its population. [23] In general, this type of meritocracy and emphasis on serving the common good is present throughout the tribe. Children are trained from birth to defend themselves and serve the tribe. [24] Training in combat and farming begins from a very early age and once the Boomers come of age, they serve in whatever capacity they are best suited. As a result, every Boomer is a highly trained combatant and a competent survivalist. [22] Having left Vault 34 and found the Nellis Air Force Base, the Boomers had to find new clothes that reflected their independence. They found old military jackets in the base and used them over their vault jumpsuits. Each jacket sports several military medals for decoration, and embroidered on the back is the number \"34,\" as to never forget where they came from. They are a self-sufficient society, producing food, weaponry, and power all inside their base. As a result, they need no relations with the outside world. They believe that self-armament is the key to a peaceful society, meaning that each Boomer carries a weapon and will not hesitate to use it when the time calls for it. The Boomers are attached to their history, whether past or present. A large fresco in their museum tells of their great epic:"
            ],
            "Notes": [
                "Pearl, the eldest Boomer and leader of the tribe, predicted that one day an outsider would get past the defenses of Nellis and help connect the Boomers with the rest of the world, even if \"only a little.\" At this point, the player character can choose to either kill Pearl (which will drop their reputation with the Boomers to Vilified) or fulfill their promise. The player character can also ignore Pearl's request. If the player character has a Liked reputation and helps out enough with the Boomers, they will be offered to raise the Lady in the Lake by Pearl. During the Second Battle of Hoover Dam , the Boomers will assist the Courier and their chosen faction by bombarding the enemy from the plane. One can actually see the plane flying and dropping the bombs. Despite the Boomers having never left Nellis Air Force Base in decades and the Courier is the first outsider they have let into their gates, NCR currency can be found in the Boomer's solar energy generator building. Despite the Boomers' outright hatred towards all outsiders, becoming not just Accepted or Liked, but Idolized is rather easy. Saying nice or intelligent things about the Boomers to Pete, turning in scrap metal to Jack, and completing their relatively simple quests/tasks all give the Courier good amounts of reputation. The Boomers are not hostile to the player character in person when first encountered. The Boomers will comment on certain companions that are currently following the"
            ]
        }
    },
    "Locations": {
        "Cottonwood Cove": {
            "Layout": [
                " only access point to the Legion's main encampment. A trio of overturned canoes rest on the shoreline, and next to them is where the boat to Dry Wells will spawn if the corresponding choice is made in the Lonesome Road add-on"
            ],
            "Background": [
                "Once a small resort location before the Great War , circa. 2281 , Cottonwood Cove was selected as the site of an outpost by Caesar's Legion , under the command of the centurion Aurelius of Phoenix . The Cove became a staging area where captives taken by the Legion are then sent by boat over the Colorado River into Arizona to be processed as slaves, as well as a launching point for Legion raids in the southern areas of the Mojave. [1] It has since become the largest single encampment of Legion forces on the western side of the Colorado River and is their foothold into Nevada , using the river to transfer troops and supplies to Fortification Hill on the east bank. [Non-game 1] The Legion was able to prevent retaliatory conflict from their enemy, the New California Republic through the actions of the frumentarius Vulpes Inculta . He orchestrated the collapse of the NCR's closest stronghold of Camp Searchlight via the unsealing of several barrels of nuclear waste that had been stored in the old fire station , enshrouding the entire area in radiation . [2] [3] When the camp fell and the NCR's presence in the region",
                " to and from Cottonwood Cove done over ham radio . Relying on the martial strength of the two contubernia at his command, Aurelius has accomplished killed and capturing a number of NCR soldiers over four times as much as that of his own forces. [5] Aurelius himself thinks of the camp's presence as a modest one, \"a single finger of the Legion reaching across the river's narrows,\" but with his forces on hand, they equate to \"an iron knuckle.\" [4]",
                "Once a small resort location before the Great War , circa. 2281 , Cottonwood Cove was selected as the site of an outpost by Caesar's Legion , under the command of the centurion Aurelius of Phoenix . The Cove became a staging area where captives taken by the Legion are then sent by boat over the Colorado River into Arizona to be processed as slaves, as well as a launching point for Legion raids in the southern areas of the Mojave. [1] It has since become the largest single encampment of Legion forces on the western side of the Colorado River and is their foothold into Nevada , using the river to transfer troops and supplies to Fortification Hill on the east bank. [Non-game 1] The Legion was able to prevent retaliatory conflict from their enemy, the New California Republic through the actions of the frumentarius Vulpes Inculta . He orchestrated the collapse of the NCR's closest stronghold of Camp Searchlight via the unsealing of several barrels of nuclear waste that had been stored in the old fire station , enshrouding the entire area in radiation . [2] [3] When the camp fell and the NCR's presence in the region waned, Aurelius crossed the Colorado and put down the Legion's roots in the Cove before beginning to arrange for raiding parties to continue disrupting NCR-allied caravans and troop movements. [4] Rather than risk sending couriers that could be intercepted, the centurion had all communication",
                "waned, Aurelius crossed the Colorado and put down the Legion's roots in the Cove before beginning to arrange for raiding parties to continue disrupting NCR-allied caravans and troop movements. [4] Rather than risk sending couriers that could be intercepted, the centurion had all communication to and from Cottonwood Cove done over ham radio . Relying on the martial strength of the two contubernia at his command, Aurelius has accomplished killed and capturing a number of NCR soldiers over four times as much as that of his own forces. [5] Aurelius himself thinks of the camp's presence as a modest one, \"a single finger of the Legion reaching across the river's narrows,\" but with his forces on hand, they equate to \"an iron knuckle.\" [4]"
            ]
        }
    }
}
from dynamic_filter import query_with_dynamic_filters
# Example JSON input
npc_json = {
    "Factions": {
        "Boomers": ["Background", "Society", "Notes"]
    },
    "Locations": {
        "Cottonwood Cove": ["Layout", "Background"]
    }
}

# Run the function to query with dynamically created filters and get the JSON object
## TO DO: combine npc_json and other json object containing convo fields
### Make prompt with json. prob ignore above
# json_object = query_with_dynamic_filters(npc_json)
# print(json_object)

### EXAMPLE 1
npc_modifiersz = {
  "npc_role": "townfolk",
  "npc_personality": "nostalgic",
  "conversation_context": "reminising on the past",
  "main_dialog_purpose": "Talking about past town history",
#   "player_reputation": "neutral",
#   "player_history": "first interaction",
  "location": "Cottonwood Cove",
  "conversation_tone": "informative",
#   "npc_name": "Sergeant Knox",
#   "player_objective": "find the hidden treasure",
  "conversation_focus": "Background NPC dialog"
}

npc_json = {
    "Factions": {
        "Boomers": ["Background", "Society", "Notes"]
    },
    "Locations": {
        "Cottonwood Cove": ["Layout", "Background"]
    }
}

npc_modifiers = {
  "npc_role": "citizen",
  "npc_personality": "depressed",
  "conversation_context": "discussing hardships about recent events",
  "main_dialog_purpose": "Talking about pain the Legion has caused",
  "location": "Cottonwood Cove",
  "conversation_tone": "Reflective",
}


x = create_prompt(MOCK_JSON_OBJECT, npc_modifiers)
print(x)