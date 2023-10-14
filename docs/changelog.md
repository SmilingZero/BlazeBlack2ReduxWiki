# Changelog (v1.4.1)                                 

## General Information

Over time, I will periodically update Redux to fix any issues that may come up and to keep the game fresh as time goes on.
!!! note
    If you find any issues with Redux, be sure to tweet them at me ([@AphexCubed](https://twitter.com/aphexcubed)) and I'll try to fix them!



## Changelog

### v1.4.1 (24/06/23) 

Balance Changes:

- Walrien line.
    - Spheal now evolves into Sealeo at level 16.
- Nerfed Normal mode Burgh's Masquerain.
   
Bug Fixes:

 - Eevee now evolves into Glaceon correctly.
 - Snorunt now evolves into Glalie correctly.


Other:

 - All Hall of Fame screens show the project's version number.

---


### v1.4.0 (24/05/23)

Balance Changes:

- Reworked Challenge mode to be significantly easier early game.
    - The style of difficulty progression is now a scaling one, with the difficulty increasing over time.
    - This should look more like Normal mode and Renegade Platinum, but still a bit harder.
    - The mid-to-late game difficulty is untouched.

As a part of this...
   
- Various important trainers have been nerfed, including:
    - The Ranch Grunt
    - No longer has as many spread moves to damage both Pokémon at once.
        - Generally has weaker moves overall now.
	- Cheren
	    - Doduo and Deerling are a little weaker now.
	- Roxie
	    - Removed Explosion on Qwilfish.
	    - Koffing now learns more level-up moves, instead of TM moves.
	    - Gastly has significantly weaker BP moves now.
	- Virbank Grunts:
	    - Nerfed Beedrill's moveset to have less coverage.
    - Brycen
	    - Swapped Delibird for a weaker Cryogonal.
	    - Reduced the BP of Smoochum's moves.
	- Sewer Grunts
	    - Dramatically lowered the BP of moves used by the grunts.
    - Burgh
	    - Swapped Yanmega for the slower and weaker Mothim.
	    - Swapped Scyther for the slower and canonical Escaviler.
	    - Swapped Durant for the slower Heracross.
	    - Broadly redid the items and moves of Burgh's team.
    - The Hoenn leaders, due to their optional nature, have been left untouched.
    - Complete details can be found in the 'Trainer Changes' document.

Pokémon which have received intended buffs:

- Venusaur line.
    - Now learns Charm at level 16.
- Eevee et al.
    - Completely redid the learnset of each member of the family.
    - Each member now gains access to elemental moves matching their strongest attacking stat early on.
    - Complete details can be found in the 'Pokémon Changes' document. 
- Victreebel line.
    - Bellsprout and Weepinbell now learn Clear Smog at level 12 and Knock off at level 30 and 33, respectively.
- Aerodactyl.
    - Now learns Dual Wingbeat at level 45.
- Typhlosion line.
    - Line now learns Flame Burst at level 22.
- Crobat line.
    - Crobat now learns Dual Wingbeat at level 1.
- Delibird.
    - Now learns Drill Peck at level 32.
- Blaziken line.
    - Now learns U-turn at level 25.
- Breloom line.
    - Shroomish now evolves into Breloom at level 21.
    - The line now has a new learnset to accommodate this.
    - Complete details can be found in the 'Pokémon Changes' document.
- Sharpedo line.
    - Carvanha now evolves into Sharpedo at level 26.
- Torterra line.
    - Now learns Sandstorm and Sunny Day at level 1.
- Infernape line.
    - Now learns Cross Chop instead of Focus Punch at level 37.
    - Now learns Focus Punch at level 1.
- Staraptor line.
    - Now learns Retaliate at level 26, instead of Uproar.
    - Staraptor now learns Sky Uppercut at level 34, alongside Final Gambit.
- Cherrim line.
    - Cherubi now evolves into Cherrim at level 18.
    - The line now has a new learnset to accommodate this.
    - Complete details can be found in the 'Pokémon Changes' document. 
- Serperior line.
    - Now learns Glare at level 22, instead of Detect.
    - Now learns Heart Stamp at level 31, instead of Mean Look.
    - Now learns Psycho Cut at level 50, instead of Glare.
- Emboar line.
    - Line now learns Slack Off at level 34.
    - Vanilluxe line.
    - Now learns Hail at level 1, instead of Mist.

Pokémon which have received intended nerfs:

- Meganium line.
    - Now learns Ingrain at level 17, instead of Reflect and Light Screen.
    - (Both screens can still be taught via TM).
- Medicham line.
    - Medicham now has stats in the Complete version: 60 HP / 65 Atk / 80 Def / 75 SAtk / 80 SDef / 90 Spd / 450 BST.
    - Swapped the levels at which Reversal and Drain Punch are learnt.

Bug Fixes:

- Corrected the listed location of the Thunderbolt TM.
- Corrected Starly and Staravia's erroneous learnsets.
- Corrected various mistakes in the Pokémon Changes document regarding evolution.

---

### v1.3.0 (21/01/23)

New Features:

- Moonblast has a new animation to better match the official animations.
    - Big thanks to @GoranConstant1 for this one!

Balance Changes:

- Wigglytuff line.
    - Now learns Nasty Plot at level 70.
- Dugtrio line. 
    - Now learns Swords Dance at level 62.
- Poliwrath line.
    - Poliwhirl now learns Waterfall at level 15, instead of Mist.
    - Poliwrath now learns Waterfall at level 1, instead of Vacuum Wave.
- Muk line.
    - Now learns Toxic Spikes at level 1, instead of Pound.
- Hypno line.
    - Now learns Recover instead of Drain Punch at levels 48 and 58 respectively.
- Quagsire line.
    - Now learns Spikes instead of Ancient Power at levels 41 and 47 respectively.
    - Now learns Toxic Spikes at level 1, instead of Mist.
- Gastrodon line.
    - Now learns Spikes instead of Amnesia at levels 40 and 45 respectively.
- Garchomp line.
    - Now learns Spikes at level 72.
- Samurott line.
    - Now learns Drill Run instead of Retaliate.
    - Now learns Sucker Punch instead of Assurance.
- Eelektross line.
    - Now learns Close Combat at level 70.
- Hydreigon line.
    - Now learns Stealth Rock instead of Focus Energy at level 1.
- Replaced Burgh's Scyther with a Larvesta on Normal mode.

Documentation:

 - Corrected Sentret's abilities in the documentation.
 - Corrected Cheren's normal mode team in the documentation.
 - Updated all the documents to v1.3.0.

Bug Fixes:

 - Juan no longer has a Wingull on Challenge mode.
 - Tate and Lisa now have the correct Pokémon on Challenge mode.
 - Eevee now evolves into Glaceon correctly.
 - Snorunt now evolves into Glalie correctly.
 - Benga now uses the correct team depending on difficulty.
 - Wave Crash now deals the correct amount of damage.
   - Various trainers have been updated accordingly to account for this!

Other:

 - Updated the 'dark' title cards.

Outstanding issues:

 - Infestation doesn't display any text when the target is hurt between turns.
    - (It is unknown currently how to fix these issues)
 - The postgame remains untouched from v1.1.1.


---

### v1.2.1 (24/08/22)


Bug Fixes:

 - Fixed a catastrophic memory issue related to the Fairy type implementation which would cause the game to crash on real Hardware and MelonDS.
 - Fixed a catastrophic issue where around 20 modified evolutions had been reverted to their vanilla methods.
    - For example, Riolu now correctly evolves again when it learns Aura Sphere, Ponyta now correctly evolves again at level 35, etc.
 - Fixed typo in the Wii Cheat Menu.
 - Fixed moves not having updated v1.2.0 effects on the White 2 Version of Redux.
 - Corrected Cheren's Normal mode levels in the documentation.
 - Swapped the level at which Medicham learns Zen Heatbutt and Psycho Cut, to reflect the buffed BP of Psycho Cut.
 - Vanilluxe is now correctly listed as learning Dazzling Gleam via TM.
 - Fixed some duplicate text regarding Shiftry.
 - The Challenge mode Ranch Grunt now has its levels correctly listed.
 - The Meditite, Bonsly, Mime Jr., Glameow and Stunky Eggs now hatch significantly faster.
 - Fixed Spheal sometimes being given by the Castelia Battle Company Egg gift.
 - Juan is no longer listed as incorrectly giving out two White Herbs on Challenge mode.
 - More small AI tweaks.

---

### v1.2.0 (20/08/22)


New Features:

 - There is now a Cheat Code system. Interact with the Wii in your house to access them.
    - These Cheat Codes include:
        - Adding Rare Candies
        - Adding Money
        - Adding Master Balls
        - Adding Berries
        - Adding the Shiny Charm
        - Adding the Oval Charm
        - Adding Max Repels
        - Adding Medicine Items
        - Adding Battle Items
        - Adding Sacred Ash
        - Adding Gems
        - Recollecting Gift Pokémon
   - Furthermore, inspired by a certain Sci-Fi franchise, there are also three Skulls:
      - Foreign: Blocks the player from receiving gift Pokémon.
      - Recession: Hides all Market Clerks and Vendors.
      - Illiterate: Hides all Move Tutors and Reminders.
   - These codes are just for fun! Enjoy breaking the game apart! :)
- HM moves can now be forgotten on the fly, without the need of a move deleter
    - (thanks totally_anonymous#0405!).

Documentation Changes:

 - The Trainer Changes document has been completely overhauled and now documents all trainers up until the Postgame.
    - Almost all trainers have new/adjusted movesets and ai, for a complete rework of what you're up against!
    - These few lines don't adequately express how fundamental and overhaul this is (there's simply too much to list here). The majority of update dev time has been spent here!
    - Special thanks to gippal#3903 for providing the documentation framework.

Trainer Changes

 - The Hoenn gym leaders have been overhauled.
    - Now they have separate Easy and Normal/Challenge mode teams, instead of Main Game/Postgame fights.
    - They now give out certain items, depending on the chosen difficulty of the fight.
    - They retain the ability to be infinitely re-battled, until the next corresponding Unova leader has been defeated.
    - Furthermore, each leader now gives out a reward for battling them. This can be infinitely recollected, so long as you continue to defeat them in battle!
        - Roxanne now gives out two Berry Juice on both Normal and Challenge Mode.
        - Brawly now gives out a Meditite Egg on both Normal and Challenge Mode.
        - Wattson now gives out two Tanga Berries on both Normal and Challenge Mode.
        - Flannery now gives out a Choice Band on Normal Mode, a dozen Cheri Berries on Challenge mode.
        - Norman now gives out a Choice Specs on Normal Mode, five Sitrus Berries and two Micle Berries on Challenge mode.
        - Juan now gives out a Choice Scarf on Normal Mode, a Air Balloon on Challenge mode.
        - Winnona now gives out an Old Amber on Normal Mode, allows the player to catch Rotom on Challenge mode.
        - Tate and Liza now give out the Protect TM on both Normal and Challenge Mode.
  

Balance Changes:

 - Added a new Egg Gift to Castelia City. Available from beating all the Battle Company staff and boss. You can obtain either:
    - Bonsly, Mime Jr., Glameow or Stunky!
 - The Swords of Justice are now all encountered at level 80.
    - This should make the three encounters suitably difficult to catch and powerful to use casually.
 - Victini's Guardian can no longer be challenged after Burgh is defeated.
    - Victini's Guardian lets the player through without a battle on Easy and Normal mode now too.
    - The Guardian will disappear once the player reaches Nacrene City in the postgame.
 - Castelia Gardens has been split into a separate met location.
 - The Route 9 Department Store is no longer a unique location from Route 9.
 - The Eviolite gift has been raised to 160 seen and to have cleared out the Battle Company, to encourage the player to fight the trainers around Castelia.
 - Bianca now heals the player before her battle in Reversal Mountain.

 - The man who gives the player the Air Balloon only appears in the postgame on Challenge mode.
 - The Grip Claw and Light Clay on (B/W version respectively) have both been replaced with a Power Herb.
 - The Protect TM on Village Bridge has been replaced with the Giga Drain TM.
 - The Giga Drain TM in Lostlorn forest has been replaced with a Grip Claw.
 - Swapped the location of Sludge Wave and a HP Up on Route 9.
 - Lagging Tail is now found in Virbank City.
 - Changed the Chesto Berry in the Trainer School to an Iron Ball.
 - Castelia City no longer sells Dusk balls or Quick balls (to make way for the missing EV berries!).
 - The Dazzling Gleam TM has been swapped with a Hyper Potion on Route 13.
 - The Hurricane TM in Mistralton City has been replaced with an Eject Button.
 - A PP Up at Victory Road's entrance has been replaced with the Hurricane TM.

 - Reverted Attack Order's stats to vanilla.
 - Raised the accuracy of Razor Shell to 100, from 95.
 - Raised the accuracy of Leaf Tornado to 100, from 95.
 - Psyshield bash now raises both Defense and Special Defense.
 - Reduced the BP of Poison Tail to 80, from 90.
 - Reduced the BP of Fly to 80, from 100.
 - Raised the accuracy of Poison Gas to 100, from 80.
 - Raised the accuracy of Stun Spore to 90, from 75.
 - Needle Arm and Rock Smash are now boosted by the ability Iron Fist.
 - Kinesis now targets both opponents in a double battle.
 - Raised the BP of Psycho Cut to 90, from 70.
 - Lowered the PP of Psycho Cut to 10, from 15.
 - The AI now uses different logic to select certain moves, hopefully making it select these moves more intelligently.


Pokémon which have received intended buffs:

 - Charizard line.
    - The line now has the ability Defiant, instead of Levitate.
    - Charmeleon is now, once again, unambiguously, part Dragon Type.
 - Blastoise line.
    - Line now learns Bubble Beam at level 22, instead of Aqua Tail.
 - Pidgeot line.
    - Moveset has been reorganised and expanded to be more useful early on.
    - Specifically, the line has slightly stronger early stab and coverage options in the midgame.
 - Raticate line
    - Learnset has been reshuffed to make it more viable against Burgh.
    - The Elemental Fangs are now learnt at level 26.
    - Now learns After You on evolution, instead of Crunch.
    - Various other moves have been shuffled around to allow for these changes.
    - Rattata has been updated similarly.
 - Arbok line.
    - Ekans now evolves into Arbok at level 21.
    - Now learns the Elemental Fangs at level 23, in place of Lunge. Lunge is now learnt at level 45.
    - Ekans has received similar changes.
    - Ekans' later moves are slightly better spaced level wise.
 - Vileplume line.
    - Now has the Thick Fat ability.
    - Oddish, Gloom and Vileplume all have new level-up learnsets.
    - These give access to better coverage moves and STAB options, whilst better fitting the level curve.
 - Venomoth line.
    - Venonat now evolves into Venomoth at level 28.
 - Golem line.
    - Swapped levels at which Wide Guard and Explosion are learnt.
    - Now learns TM93 Wild Charge.
    - Golem now learns Head Smash at level 66.
 - Muk line.
    - Grimer now has stats in the Complete version: 80 HP / 80 Atk / 50 Def / 40 SAtk / 70 SDef / 25 Spd / 345 BST.
 - Electrode line.
    - Swapped levels at which Thunder Shock and Spark are learnt.
    - Swapped levels at which Thunder Wave and Rollout are learnt.
 - Weezing line.
    - Swapped levels at which Toxic Spikes and Lava Plume are learnt.
    - Swapped levels at which Pain Split and Sludge are learnt.
 - Mr. Mime line.
    - Mime Jr. now evolves into Mr. Mime at level 25, rather than via happiness.
    - The line's learnset has been completely revamped, on account of it being a guaranteed encounter now.
        - This includes an emphasis on support tools for Burgh, such as Fake Out, Follow Me, Heal Pulse, Healing Wish, Hypnosis and Trick.
	    - Now compatible with the Mystical Fire TM, like in L:A.
 - Feraligatr line.
    - Croconaw now has stats in the Complete version: 75 HP / 80 Atk / 80 Def / 49 SAtk / 68 SDef / 53 Spd / 405 BST.
    - Now learns Rock Tomb by level-up instead of Ancient Power.
    - Now learns Raging Fury by level-up instead of Water Pulse.
    - Slightly shuffled level-up moves between levels 20 and 28.
    - Swapped levels at which Agility and Aqua Tail are learnt.
    - Swapped levels at which Crunch and Wave Crash are learnt.
    - Now learns Focus Punch from the move learner.
 - Ariados line.
    - Ariados now learns Psychic Fangs at level 1.
 - Ampharos line.
    - Ampharos is now compatible with the Energy Ball TM. (for @hectorama501st)
    - The line has a new moveset with some important buffs to facing Burgh, namely Electroweb and Discharge.
 - Bellossom.
    - Now has the Cloud Nine ability.
    - Now has a new, expanded level-up learnset, featuring some new tools for Burgh like Fiery Dance.
 - Sudowoodo line.
    - Bonsly now evolves into Sudowoodo at level 25, rather than via happiness.
    - The line's learnset has been completely revamped, on account of it being a guaranteed encounter now.
         - This includes an emphasis on offensive tools for Burgh, such as Rock Tomb, Foul Play, Sucker Punch, the Elemental Punches and Stone Edge.
 - Jumpluff line.
    - Swapped the levels at which Stun Spore and Rage Powder are learnt.
    - Hoppip now has stats in the Complete version: 35 HP / 35 Atk / 40 Def / 45 SAtk / 55 SDef / 70 Spd / 280 BST.
    - Skiploom now has stats in the Complete version: 55 HP / 45 Atk / 50 Def / 55 SAtk / 65 SDef / 90 Spd / 360 BST.
    - Skiploom and Jumpluff can now learn HM02 Fly.
 - Sunflora line.
    - Sunkern now has stats in the Complete version: 50 HP / 30 Atk / 50 Def / 30 SAtk / 50 SDef / 30 Spd / 240 BST.
 - Espeon.
    - Now learns TM22 Solar Beam.
 - Umbreon.
    - Now learns TM36 Sludge Bomb.
 - Ursaring line.
    - Teddiursa is now part Ground type, like Ursaring.
    - The line now learns Bulldoze at level 16, instead of Curse.
    - The line now learns Curse at level 7, instead of Focus Energy.
 - Smeargle.
    - Now learns all TMs and all HMs (from the disks, without need needing to use Sketch).
 - Blaziken line.
    - Now learns Agility by level up, instead of Bounce (which can be learnt via move tutor).
 - Swampert line.
    - The line now has the ability Water Veil, over Anticipation.
 - Swellow line.
    - Swapped the levels at which Mimic and After You are learnt.
 - Masquerian line.
    - Masquerain no longer has the Levitate ability.
    - The line has a new learnset to be more effective against Burgh, including Tailwind, Air Cutter and Bubble Beam.
 - Exploud line.
    - Now learns Chatter instead of Roar at level 26.
 - Delcatty line.
    - Skitty now evolves into Delcatty at level 25, rather than with a Moon Stone.
    - Delcatty now has stats in the Complete version: 70 HP / 95 Atk / 65 Def / 85 SAtk / 75 SDef / 95 Spd / 485 BST.
 - Medicham line.
    - The line's learnset has been completely revamped, on account of it being a guaranteed encounter now.
    - This has been done with a greater focus on offensive utility and breaking power, with moves like Focus Punch, Drain Punch, Rock Tomb and Fake Out.
 - Manectric line.
    - Manetric is now compatible with the Energy Ball TM. (for @hectorama501st)
    - The line has an expanded learnset, so that the line hasn't learnt all its moves by Clay/Skyla.
 - Swalot line.
    - Now has an expanded learnset with a focus on options for Burgh and better starting moves.
 - Torkoal.
    - On both the Complete and Classic version, Shell Armor is now a regular ability and White Smoke a Hidden ability. 
 - Cacturne line.
    - Swapped the level at which Switcheroo and Destiny Bond are learnt.
    - Now learns Sandstorm at level 20, instead of Grass Whistle.
 - Seviper.
    - Now learns Power Whip at level 58.
 - Lunatone.
    - Now has a brand new learnset to lean into the Pokémon's Lunar theme.
 - Solrock.
    - Now has a brand new learnset to lean into the Pokémon's Solar theme.
 - Whiscash line.
    - Now learns TM93 Wild Charge.
 - Kecleon.
    - Now as the ability Adaptability in the Complete version of Redux.
 - Walrein line.
    - Spheal now evolves into Sealeo at level 21.
    - The line's learnset has been redone to make it more valuable early on.
        - Important additions include Slack Off and Bubble Beam.
 - Relicanth.
    - Now learns Rock Slide at level 25.
 - Metagross line.
    - The line's learnset has been been redone and expanded.
        - Important additions include Shift Gear and Heavy Slam.
    - Metang and Metagross now have Heavy Metal as their hidden ability, rather than Light Metal.
 - Cherrim line.
    - Cherubi now has stats in the Complete version: 55 HP / 35 Atk / 60 Def / 62 SAtk / 53 SDef / 40 Spd / 300 BST.
 - Purugly line.
    - Glameow now evolves into Purugly at level 27.
    - The line's learnset has been completely revamped, on account of it being a guaranteed encounter now.
        - This includes an emphasis on fast utility for Burgh, such as U-Turn, Fake Out, Quick Attack, Knock Off, Hypnosis and Aerial Ace.
 - Stuntank line.
    - Stunky now evolves into Stuntank at level 27.
    - The line's learnset has been completely revamped, on account of it being a guaranteed encounter now.
        - This includes an emphasis on bulky offense for Burgh, such as Acid Spray, Poison Jab, Flamethrower, Knock Off, Assurance and Snarl.
 - Chatot.
    - Chatot's learnset has been expanded to better fit the level curve.
 - Lumineon line.
    - Swapped levels at which Soak and Hydro Pump are learnt.
    - Slightly shuffled Captivate, Aurora Beam, Safeguard and replaced Safeguard with Icy Wind.
 - Serperior line.
    - Now learns Detect at level 22, instead of Coil.
 - Stoutland line.
    - Now has its Gen VIII Attack stat of 110.
    - Stoutland now has stats in the Complete version: 95 HP / 110 Atk / 90 Def / 45 SAtk / 90 SDef / 80 Spd / 510 BST. 
 - Unfezant line.
    - The lines learnset has been redone, to prioritise strong moves earlier.
    - Pidove now has stats in the Complete version: 50 HP / 36 Atk / 50 Def / 55 SAtk / 30 SDef / 43 Spd / 264 BST.
    - Tranquill now has stats in the Complete version: 65 HP / 50 Atk / 65 Def / 77 SAtk / 42 SDef / 66 Spd / 365 BST.
    - Unfezant now has stats in the Complete version: 80 HP / 65 Atk / 80 Def / 110 SAtk / 55 SDef / 95 Spd / 485 BST.
 - Audino.
    - In the Complete version of Redux, the ability Healer is replaced with Natural Cure.
 - Leavanny line.
    - Swapped the levels at which Leavanny learns Me First and Air Slash.
 - Darmanitan line.
    - In the Complete version of Redux, the ability Hustle is replaced with Sheer Force on Darumaka.
 - Crustle line.
    - Now learns Rock Tomb at level 8, instead of Smack Down.
    - Now learns Rock Slide at level 24, instead of Rock Tomb.
 - Garbodor line.
    - Now learns Wide Guard instead of Double Slap.
    - Swapped levels at which Recycle and Rock Blast are learnt.
    - Trubbish now has stats in the Complete version: 65 HP / 50 Atk / 62 Def / 45 SAtk / 62 SDef / 65 Spd / 349 BST.
 - Sawsbuck line.
    - Sawsbuck now has stats in the Complete version: 85 HP / 110 Atk / 70 Def / 60 SAtk / 70 SDef / 95 Spd / 490 BST.
 - Basculin.
    - Basculin now has stats in the Complete version: 90 HP / 102 Atk / 65 Def / 90 SAtk / 55 SDef / 98 Spd / 500 BST.
 - Carracosta line.
    - Line now learns Razor Shell at level 21 instead of Brine.
 - Vanilluxe line.
    - Vanilluxe is now part Fairy Type.
    - Vanilluxe's learnset has been updated to reflect this change.
 - Beheeyem line.
    - Now learns Trick Room at level 1, to better communicate the line's niche to the average player.
    - Now learns Psybeam at level 21.
    - Now learns Mystical Fire at level 27.
    - Swapped the levels at which Role Play and Trick are learnt.
 - Beartic line.
    - Beartic now has stats in the Complete version: 105 HP / 130 Atk / 80 Def / 70 SAtk / 80 SDef / 55 Spd / 520 BST.


Pokémon which have received intended nerfs:

 - Venusaur line.
    - The line now has the ability Solar Power, instead of Thick Fat.
    - Venusaur now has stats in the Complete version: 80 HP / 87 Atk / 85 Def / 103 SAtk / 100 SDef / 80 Spd / 535 BST.
 - Fearow line.
    - Spearow now evolves into Fearow at level 21, up from level 20.
    - This is intended to stop a potential encounter over-centralisation in the Brawly fight on Challenge mode.
    - Spearow itself has gained Intimidate as an ability on the Complete version of Redux.
 - Raichu line.
    - Pichu and Pikachu now learn Spark at level 12, instead of Shock Wave.
    - Pichu and Pikachu now learn Wish at level 14, instead of Charm.
    - Starting with Agility, Pikachu's learnset has been slightly spaced apart level-wise to better fit Redux's level curve.
    - Raichu now has a slightly expanded learnset, now learning Shock Wave at level 25, Reversal at level 45 and Volt Tackle at level 65.
 - Gengar line.
    - The learnset has been slightly reshuffed to better fix the level curve of Redux and to cut down on level 1 moves.
    - The line has gained Poison Gas early, but Nasty Plot has notably been delayed.
 - Starmie line.
    - In both the Complete and Classic version of Redux, Staryu and Starmie have Analytic now as the first ability.
    - This replaces Illuminate and Regenerator, respectively.   
 - Meganium line.
    - No longer learns Earth Power, instead learns Draining Kiss from the move learner.
    - Now learns Mega Drain at level 22.
    - Now learns Heal Pulse at level 28.
    - Now learns Nature Power at level 31.
    - Now learns Aromatherapy at level 43.
    - Now learns Magic Coat at level 46.
    - Now learns Leech Seed at level 54.
    - Swapped levels at which Solar Beam and Moonblast are learnt.  
    - Similar changes have been made to Chikorita and Bayleef.   
 - Crobat line.
    - Swapped levels at which Super Fang and Wide Guard are learnt.
    - These changes have been applied to Zubat and Golbat.
 - Hitmontop.
    - Swapped levels at which Double-Edge and Wide Guard are learnt.
 - Tyranitar line.
    - Now learns Dark Pulse at level 31, instead of Protect.
 - Roserade line.
    - Swapped levels at which Magical Leaf and Mega Drain are learnt.
    - Swapped levels at which Venoshock and Leech Seed are learnt.
    - Roselia now learns Leaf Tornado at level 27, instead of Seed Bomb.
    - Roserade's level 1 learnset has been expanded to encompass more of its pre-evolution's moves.
    - This includes Leech Seed, Spikes and Toxic Spikes.
 - Lopunny line.
    - Learnset has been completely rebalanced. Now has a sensible progression in power as you progress through the game.
 - Mismagius line.
    - Mismagius now has stats in the Complete version: 60 HP / 64 Atk / 66 Def / 105 SAtk / 105 SDef / 95 Spd / 495 BST.
 - Garchomp line.
    - Swapped the level at which Scorching Sands and Sandstorm is learnt.
 - Magnezone line.
    - How has a rebalanced learnset. Previously shortly after evolution into Magneton, the line learned all its best moves straight way. 
    - There's now a steady progession of moves, which also better accommodate the level curve.
    - The learnset before this point is largely unchanged.
 - Rotom.
    - Rotom-Fan now has the ability Motor Drive.
 - Conkeldurr line.
    - Learnset has been completely revamped. 
    - Mainly, Detect has been removed, Wide Guard pushed back and the order in which fighting moves are learnt is more sensible.
 - Chandelure line.
    - Swapped the levels at which Acid Armor and Ally Switch are learnt.
 - Mienshao line.
    - Learnset has been completely revamped, removing the over abundance of TM and Tutor moves in the learnset.


Pokémon which have have received neutral changes/have received minor changes:

 - Arcanine line.
    - Swapped levels at which Close Combat and Flare Blitz are learnt on Arcanine.
 - Typhlosion line.
    - Typhlosion now learns Lava Plume again (Technically a bugfix).
 - Azumarill line.
    - Now evolves at level 21. (Technically a bug fix)
    - Swapped the level at which Helping Hand and Aqua Jet are learnt for Marill and Azumarill.
 - Wobbuffet line.
    - Now learns Amnesia (an event move) and Tickle.
    - Flattened Wynaut's learnset to level 1.
 - Steelix line.
    - Now learns Autotomize at level 44.
    - Wide Guard is now learnt larger, with Heavy Slam slightly pushed back to accommodate.
    - Swapped levels at which Rock Blast and Dragon Dance are learnt.
    - Now learns Rollout at level 13.
    - Now learns Dragon Dance at level 68.
    - Steelix now learns Iron Tail instead of Dragon Tail at level 37.
    - (Onix has been nerfed, Steelix slightly buffed).
 - Donphan line.
    - Donphan has been regifted Water Gun from Gen II. Now it can play in the puddles again <3.
 - Wailord line.
    - No longer has the Drizzle ability. (Gained it purely for Marlon on old Challenge mode to have another weather setter, kinda pointless now.)
    - Wailord now has stats in the Complete version: 200 HP / 90 Atk / 45 Def / 90 SAtk / 45 SDef / 60 Spd / 530 BST
    - Now can learn Wide Guard, Boomburst and importantly Final Gambit.
    - Has a new level-up learnset to accommodate this.
    - Loosing Drizzle is never gonna be easy, but the addition of Final Gambit should rule Wailord out as being useless!
 - Anorith, Lileep, Nosepass and Archen now all give 65 Base Exp (Down from 70-something each).
    - This is intended to make defeating Roxanne slightly easier to Exp manage.
 - Toxicroak line.
    - Updated learnset to cut down on level 1 moves and to better match the level curve of Redux.
 - Magmortar line.
    - Magmar and Magmortar now share a learnset. (Technically a bugfix, since levels between the two of learnt moves didn't match).
    - The learnsets have been expanded to better fix the level curve.
    - Magmortar is now compatible with Sludge Bomb.
 - Electivire line.
    - Electabuzz and Electivire now share a learnset. (Technically a bugfix, since levels between the two of learnt moves didn't match).
    - The learnsets have been expanded to better fix the level curve.
 - Musharna line.
    - Learnset has been completely revamped, focusing on bringing niche moves to the forefront, like Magic Room and Wonder Room.
 - Gigalith line.
    - Shuffled the levels at which Wide Guard and Explosion are learnt.
    - Now learns Rock Wrecker.
 - Swoobat line.
    - Woobat now evolves into Swoobat at level 25, rather than by happiness.
    - Completely rebalanced the lines learnset to lean more into the Simple ability.
    - Swoobat is no longer compatible with the Power Gem TM.
 - Hydreigon line.
    - Removed duplicate Body Slam from Deino and Zweilous (Technically a big fix).


The following Wild Areas have received changes:

- Aspertia City and Route 19 now have Surskit as an encounter when fishing, rather than Poliwag.
- Shellder is no longer found on Route 20 in Winter, instead Dratini can be found all year long.
    - Dratini is also slightly more common now.
- Raised odds of obtaining Stunfisk by fishing in Castelia Sewers.
- The Seaking line is no longer found in Lostlorn Forest, instead you will now find Psyduck.
- Shellder is no longer found on Route 6.
- Aron is now found in the Route 6 Hidden Grotto (by Mistralton Cave), instead of Woobat.


Bug Fixes:

 - Burmy now has the correct level-up moves.
 - Triple Axel now has the correct BP.
 - Fearow's learnset now matches the documents.
 - Grepa and Tamato Berries are now correctly obtainable in Castelia City.
 - Correctly documented Relicanth's abilities.
 - Changed an Ace Trainer in Chargestone Cave so you can still progress without reloading the area.
 - Poochyena's abilities are now correct to the documents.
 - Nosepass's abilties are now consistent between evolutions.
 - Join Avenue is correctly unblocked on Easy and Normal Mode.
 - Sneasel no longer has the ability Technician.
 - Seedot's abilities are now correctly documented.
 - Fixed crash when encountering Arceus.
 - The opening cutscene now has the correct cry for Shaymin.
 - Fixed some wonky maths in Virbank City's Surf encounter table.
 - Mystical Fire now correctly only targets a single opponent.
 - Blizzard is now 110BP like in vanilla.
 - Swagger now correctly Paralyses the target.
 - Yanma now correctly learns Giga Drain by TM.
 - Nidoqueen's stats are now correct to Gen VIII.
 - Haxorus now correctly learns Close Combat by level up.
 - Corrected Pawniard's evolution level.


Documentation:

 - Piloswine is now spelt correctly in the Evolution Changes document.
 - The Gift Pokémon document is more clear in what ability the Unova starters have.


Outstanding issues:

 - Postgame stuff. As mentioned on my Twitter, the Postgame has been left out of v1.2.0 in order to get the update out faster. These small, non-gamebreaking issues remain.
    - There's a bunch of duplicate TMs in the postgame.
    - Deoxy's event still doesn't work. 
        - As a work around just now, Deoxys appears after you reach Nacrene City, but the surrounding event doesn't work.
    - There's a couple of Cut trees still strewn about.
    - Wallace and Steven haven't yet been updated to the new Hoenn Leader standard of v1.2.0.
 
 - Wave Crash doesn't do the correct amount of damage, it's currently bugged to be Base 60 in power.
 - Infestation doesn't display any text when the target is hurt between turns.


Other:

 - Relabelled the different difficulty modes of Redux, to better communicate the intentions of each to the player.

---

### v1.1.1 (22/05/22)

Balance Changes:

 - Aron is now found Relic Passage, Castelia side. (for @pponli)

Bug Fixes:

 - Castelia Grass rates (my new reoccurring foe) should, finally, once and for all, actually be raised and not lowered.
 - Unity Tower should no longer crash on Hardware or MelonDS, for real now.
 - Weavile no longer has Technician, as promised. It has also regained Triple Axel.
 - Fearow's BST. is now correct to the documents.
 - Noctowl's BST. is now correct to the documents.
 - Farfetch'd's documented total BST. is now correct.
 - The Vanillite line now correctly matches the documentation in various aspects.
 - The Pledge moves now have the correct BP.
 - The documentation now correctly states that Staravia has Intimidate.
 - Arceus can no longer be summoned to your mortal realm an infinite number times (Well, without chatting to me first, that is).
 - Fixed a crash in the Nature Preserve (although fortunately no-one has reported having been effected by it!).
 - Shuppet and Banette can now learn Gunk Shot via move tutor.
 - Riolu's learnset now matches the documents.
 - Charizard, Ampharos, Sceptile and Servine can now learn Draco Meteor via move tutor.
 - Politoad now correctly learns Earth Power via move tutor.
 - Abomasnow now correctly learns Earth Power via move tutor.
 - Shiftry now correctly learns Heat Wave via move tutor.
 - Skull Bash has been updated to Gen VIII stats.
 - Arm Thrust BP now matches the documents.
 - Strength now has the correct BP.
 - Tyrogue now correctly matches abilities when it evolves.
 - Breloom now correctly learns Fake Tears instead of Fake Out.
 - Registeel now learns Iron Head at the correct level of 42, not level 81.
 - Kyurem (base form) now has the correct ability, Pressure.
 - The Magby line now learns Mach Punch and Screech at the correct levels.
 - Fixed the Subway Masters.
 - The Link Cable now functions correctly.

Documentation:

 - Xatu now has the correct total BST. for its vanilla form.
 - Dual Chop and Dual Wingbeat are now correctly documented.
 - Updated all the documents to v1.1.1.
 - The Item Changes document now correctly accounts for the shift in Blizzard, Fire Blast and Thunder TMs.

---

### v1.1.0 (20/05/22)


New Features:

 - Several boss fights have new music! (Big thanks to Dray for getting this working, I wasn't able to in development!)
 - Hidden Grottos now spawn a new Pokémon every single time you enter.
    - Grotto encounter tables have been overhauled to account for this.
 - Shaking Grass/Water Bubbles/Shaking Sand now spawns with a higher frequency.
 - On Easy and Normal mode, the player can now receive the gift Eevee in Castelia before the postgame.
 - In the postgame, the player can now obtain additional Unovan starters as gifts.
    - Furthermore, interacting with this will reset the other starter gifts, allowing them to be collected again.
 - All Shiny-locks have been removed.

Balance Changes:

 - Added Permanent Sandstorm to the Clay fight, on Challenge Mode. (This is like Crasher Wake's Gym in Renegade Platinum!)
 - The old Choice item blocker has now been repurposed to guard the Blizzard, Fire Blast and Thunder TMs.
    - All three Choice Items are now available in the Postgame.
    - The vendor which sells the three aforementioned TMs no longer exists!
 - Redid trainers in Chargestone Cave.
 - Redid trainers on Route 7.
 - Redid trainers in the Abundant Shrine.
 - Shuffled the trainers in Skyla's gym around, the majority are mandatory and two can be avoided with careful movement.
 - Nerfed Blaze Kick, Brutal Swing, Dual Chop, Dual Wingbeat and Strength.
 - Buffed Raging Fury a little.
 - Swapped Power-Up Punch and Rock Smash TM locations, to incentivise exploring Virbank Complex.
 - Swapped Giga Drain and Grass Knot TM locations.
 - Swapped Trick Room and Quash TM locations.
 - Swapped Aura Sphere and Explosion TM locations.
 - Gems can no longer be obtained from cave Dust Clouds.
 - A Chesto Berry is given out in the Trainer School.
 - Aspear, Oran and Rawst Berries can now be purchased in Virbank City.
 - Pecha, Chesto Berries can now be purchased in Castelia City.
 - The Café Sonata bartender now gifts the player Berry Juices, instead of Moomoo Milk.
 - Figy, Wiki, Mago, Aguav and Iapapa Berries can now be purchased in Driftveil City.
 - Sitrus and Perism Berries can now be purchased in Humilau City.
 - Added a blocker to the Entralink Missions. On Challenge Mode, these are only accessible after Clay now.
 - Blocked Join Avenue vendors on Challenge Mode.
 - On Challenge Mode, the player's team is now healed before Gym fights and before entering the Pokémon League.

Pokémon which have received buffs:

 - Venomoth line.
 - Jumpluff line.
 - Girafarig.
 - Magcargo Line.
 - Shiftry line.
 - Plusle.
 - Minun.
 - Sharpedo Line.
 - Camerupt line.
 - Cacturne line.
 - Tropius.
 - Relicanth.
 - Rampardos line.
 - Electivire line.
 - Magmortar line.
 - Mamoswine line.
 - Gallade.
 - Probopass Line.
 - Serperior line.
 - Emboar line.
 - Liepard line.
 - Unfezant line.
 - Leavanny line.
 - Sawk.
 - Basculin.
 - Vanilluxe Line.

Pokémon which have received nerfs:

 - Venusaur line.
 - Fearow line.
 - Rapidash line.
 - Farfetch'd.
 - Marowak line.
 - Jynx line.
 - Typhlosion line.
 - Furret line.
 - Sceptile line.
 - Gardevoir.
 - Medicham line.
 - Infernape line.
 - Staraptor line.
 - Lopunny line.
 - Mismagius line.
 - Weavile line.
 - Archeops Line.
 - Zoroark line.

Pokémon which have been reworked/have received minor changes:

 - Charizard line.
 - Blastoise line.
 - Primeape line.
 - Poliwrath line.
 - Cloyster line.
 - Kabutops line.
 - Ledian line.
 - Ursaring line.
 - Mightyena line.
 - Lucario line.
 - Samurott line.
 - Simisage line.
 - Simisear line.
 - Simipour line.
 - ZeBST.rika line.
 - Gigalith line.
 - Ferrothorn line.
 - Eelektross line.
 - Beartic line.
 - Cobalion.
 - Terrakion.
 - Virizion.

The following important trainers have received changes:

 - Cheren, Challenge Mode.
 - Roxanne, all Modes.
 - Roxie, Challenge Mode.
 - Brycen, Challenge Mode.
 - Elesa, Challenge Mode.
 - Rood, all Modes.
 - Norman, all Modes.
 - Clay, Challenge Mode.
 - Skyla, Challenge Mode. 
 - Drayden, Challenge Mode.
 - Marlon, Challenge Mode.
 - Colress, all Modes, Plasma Frigate battle.
 - Weather Trainers, all Modes.
 - Grimsley, Challenge Mode.
 - Caitlin, Challenge Mode.
 - TM Protectors, Challenge Mode.
 - Various Hoenn leaders.

Various minor trainers have been moved around/have received changes.

The following Wild Areas have received changes:

 - Route 20.
 - Virbank Complex (Inner).
 - Route 4.
 - Relic Passage.
 - Desert Resort (Inside).
 - Route 5.
 - Route 16.
 - Lostlorn Hidden Grotto.
 - Driftveil Drawbridge.
 - Clay Tunnel.
 - Chargestone Cave.
 - Mistralton Cave.
 - Celestial Tower.
 - Reversal Mountain.
 - Undella Town.
 - Adundant Shrine.
 - Seaside Cave.
 - Route 9.
 - Giant Chasm.
 - Victory Road.

Bug Fixes:

 - Raised the encounter rates for the Castelia City grass, again.
 - Reversal Mountain on Black 2 is no longer broadly skippable.
 - Unity Tower should no longer crash on Hardware or MelonDS.
 - The Darmanitan 'statue' should no longer crash on Hardware or MelonDS.
 - Fixed the text of the Cones and Boulders outside Twist Mountain.
 - Budew is now obtainable outside of the Egg Gift.
 - Deoxys should no longer appear early at the Giant's Chasm.
 - Knocking Dialga out should no longer bar the player from the new storyline.
 - Fixed the 'Red Fog of Terror 3' movie in Pokéstar Studios.
 - Fixed the position of the Medal Man in White Forest.
 - An Old Woman in Lentimas Town no longer refers to the Cleanse Tag as the Spell Tag.
 - Village Bridge signs no longer crash the game on interaction.
 - Gifted names to the TM protectors.
 - Latios now flees in good spirits.
 - Fixed a ghostly item ball on Route 17.
 - Removed the duplicate Giga Drain TM on Route 18.
 - B/W Kyurem is once again level 70.
 - Added the Rose Incense to the Route 9 Shopping Mall.
 - Link Cables are no longer found in Cave Dust.
 - Fixed some crashy cones in Twist Mountain.
 - Fixed 'Clair Clair'.
 - Persian, Flygon and Swanna's BST. is now correct to the documents.
 - Corrected Magnezone's abilties.
 - Corrected Luxray's typing on the Classic Version.
 - Rotom now correctly learns Nasty Plot.
 - Corrected Mamoswine's experience curve.
 - Darmanitan Zen now learns the correct moves.
 - Gliscor now correctly learns Rock Climb by TM.
 - Slowking now correctly learns Waterfall by HM.
 - Gyarados now correctly learns Raging Fury by level.
 - Kingdra now correctly learns Hurricane by TM.
 - Metang now correctly learns Fly by HM.
 - Metagross now correctly learns Fly by HM.
 - Farfetch'd now correctly learns a number of new moves by TM/HM.
 - Bibarel now correctly learns Swords Dance by TM.
 - Chatot now correctly learns Bug Buzz by TM.
 - Cloyster now correctly learns Waterfall by HM.
 - Made Togepi Normal/Fairy and documented this correctly.
 - Glaceon now correctly learns Dazzling Gleam by TM.
 - Articuno now learns correctly learns Sheer Cold.
 - Fixed Disarming Voice, now hits both targets again.
 - Dual Wingbeat can now correctly reach across the field in a Triple battle. 
 - Chatter now can now correctly confuse targets.

Documentation:

 - Expanded the recommended level caps to include boss fights new to Redux.
 - Explicitly noted that Audino doesn't carry Oran or Sitrus Berries. (Removed to help with wild Audino grinding.)
 - Fixed ability mismatches for Dustox, Lopunny and Escaviler.
 - Documents no longer list Charmeleon as a Fire/Flying nor a Fire/Dragon type.
 - Various fixes to the Pokémon Changes document.
 - Updated all the documents to v1.1.0. 

Other:

 - Updated the Hall of Fame screen so that which ever screen you use, the version number is present.

---

### v1.0.2 (02/04/22) 

This patch is somewhat compatible with older saves. To update, simply patch a Vanilla Rom with the Complete version of Redux as before, and then any optional patches.

So long as you name the new patched file the same thing as the old patched file, your save will carry over.

If you need help patching the game, please read the Patching Guide document.

However, to ensure complete save compatibility, you will need to go back and redo all the new E4 meetings, if you've already seen them.

 They are found on:

 - Driftveil Drawbridge.
 - Twist Mountain entrance, Route 7.
 - Undella Town.
 - Opelucid Gate.

However, if you have already completed the Route 7 event and not the others, your save is sadly incompatible and you will need to restart.

It should also be noted that old saves will still see Deoxys erroneously in the Giant Chasm - just ignore him! New v1.0.2 saves won't have this issue.


Balance Changes:

 - Seismitoad now learns Waterfall, at special request :)
 - Raised the encounter rates for the Castelia City grass.

Bug Fixes:

 - Fixed the Castelia Clowns incorrectly still referring to the Shiny Charm.
 - Fixed Lenora's a.i. so that she doesn't harm her partner Hawes.
 - Fixed Nidoking accidentally learning Poison Sting, over Poison Tail.
 - Nidoking now correctly learns Play Rough by TM.
 - Fixed Block's animation hanging the game.
 - Fixed Mewtwo not disappearing after battle.
 - Fixed Mienfoo and Larvesta evolving early.
 - Fixed Psyduck and Vanillite evolving too late.
 - Fixed Gligar's evolution and changed Sneasel's to match.
 - Fixed Misdrevous having incorrect stats, as a holdover from the original BB2 and VW2.
 - Fixed the Gothita line's abilities to match the documents.
 - Fixed a nasty issue where some of the new events won't fire, which softlocks the player at Skyla. (This is reminiscent of the Safari Zone bug in SGSS v1!)
 - Fixed some wonky text in Floccesy Town.
 - The Castelia Back Alley trainers have had their levels and teams corrected.
 - Murkrow and Honchkrow can now learn Night Slash, like in Vanilla.
 - Smoochum now correctly learns Heart Stamp, over Heart Swap, as in the documents.
 - Fixed the crashy boulders on Route 7.
 - Fixed the crashy cones blocking Pokestar Studios.
 - Fixed Hugh's ai being very passive towards the player.
 - Fixed Colress' ai being very passive towards the player.
 - Fixed an issue with the game crashing on Volt White 2 version upon viewing a Pokédex entry.
 - Fixed Deoxys appearing early, like in the original BB2 and VW2.
 - Fixed Bianca's trigger so that she correctly isn't avoidable.
 - Raised Bianca's levels slightly, previously incorrectly lower than Skyla's on Challenge Mode.
 - Raised Hugh's levels slightly outside Chargestone Cave and in Undella town, for similar reasons to Bianca.
 - Giant Chasm has had some leftovers from the original BB2 and VW2 cleaned out.
 - Giant Chasm should no longer crash on Hardware or MelonDS.
 - The Abundant Shrine should no longer crash on Hardware or MelonDS.
 - Dragonspiral Tower should no longer crash on Hardware or MelonDS.
 - Moor of Icirrus should no longer crash on Hardware or MelonDS.
 - The climax of the new Postgame story should no longer crash on Hardware or MelonDS.
 - Route 18 should no longer crash on Hardware or MelonDS.
 - Fixed some blank dialogue in Café Sonata.
 - Fixed some blank dialogue in outside Unity Tower.
 - Fixed Ledian's Fly compatibility.
 - Fixed the Striaton City Gym Trio's teams.
 - Cloyster now correctly learns Waterfall.
 - Adjusted the learnsets on Volbeat and Illumise, removed Fairy Wind from Illumises learnset, since it doesn't exist in Redux.
 - Fixed Hugh on Route 20 behaving strangely.
 - The rain Weather Trainer's Politoad now correctly has Drizzle as an ability.
 - Fixed the Winter Route 6 fishing encounters, also updated the Documents to reflect this.
 - Removed the old BB2 and VW2 legendary activator in Humilau City.
 - Freed a poor Hiker from a wall in Reversal Mountain.
 - Fixed Burgh's Dwebble on Normal Mode holding Leftovers instead of an Eviolite.
 - Fixed some minor errors in moves for the Reversal Mountain trainers.
 - Claydol no longer learns erroneous moves.
 - Fixed a typo in Bianca's Aspertia City dialogue.
 - Fixed the Blue haired lady on Route 5's text.
 - Fixed Crunch, now again correctly lowers defense.
 - Fixed Play Rough, now correctly lowers attack.
 - Fixed Rhydon appearing in Relic Passage.
 - Fixed Klang not appearing in Chargestone Cave.
 - Omanyte now correctly learns Power Gem by TM.
 - Fixed a text issue in Clay's trainer, one of the trainers previously referenced his old vanilla team.
 - Fixed Lenora's text in Nacrene Museum.
 - Fixed an NPC in Opelucid having no dialogue.
 - Removed Huge Power on Igglypuff, to remain constant with Jigglypuff.
 - Lumineon can now learn Hurricane as the documents suggest.
 - Fixed a sign outside Lacunosa Town ambushing the reader and crashing the game.
 - Fixed a nasty issue where the new moves like Nuzzle and Scorching Sands didn't correctly apply their status effect.
 - Fixed Scolipede Time!

Documentation Changes:

 - Noted that NDS forwarder doesn't work with Redux.
 - Updated the Trainer Changes to fix a handful of errors.
 - Fixed the order of Cubchoo's abilities in the documents.
 - Updated all the documents to v1.0.2.
 - Updated the Move Changes document to include some previously undocumented changes.
 - Included Shellder on the Type Changes document.
 - Fixed the Clay Tunnel entry in the Wild Area Changes document incorrectly listing Boldore twice.
 - Boldore's new evolution method is now correctly documented.

Other:

 - Updated a swath of item names to match modern standards.

---

### v1.0.1 (27/03/22)

Day one patch of Redux.

This patch is compatible with older saves. To update, simply patch a Vanilla Rom with the Complete version of Redux as before, and then any optional patches.

So long as you name the new patched file the same thing as the old patched file, your save will carry over.

If you need help patching the game, please read the Patching Guide document. 

Balance Changes:

 - Updated the Ranch Egg gift so that the eggs don't hatch instantly (but still quickly), so that the player has some agency on where to hatch them.
 - Swapped Bug Buzz and Fury Cutter on Kricketune, so that players don't get hung up on reseting for Kricketot.
 - Updated Butterfree and Beedrill's learnsets so that Confusion and Gust etc aren't locked to the move relearner.
 - Pushed Huge Power back on Jigglypuff, now only available as a Wigglytuff.
 - Shuffled Jigglypuff's moves for better pacing the learnset progression of the line (e.g. you don't get all the best moves straight away).
 - Removed Dragon typing from Charmeleon.
 - Swapped the levels that Blitzle learns Spark and Screech.
 - Swapped Pikachu and Pachirisu on Route 5.
 - Swapped Clear Smog for Haze on Litwick.
 - Swapped Tail Slap for Double Hit and dropped Technician for Skill Link on Challenge Mode Cheren's Aipom. This should make the AI a bit better, as well as feeling less unfair if the AI unleashes a 120+ BP move on you!
 - Reduced the odds of guaranteed Happiny or Togepi in the Shaking Ranch Grass.
 - Shuffled Cubchoo's moves around so it's more in line with its peers power-wise.
 - Swapped Acrobatics on Pansage to be consistent with the other Elemental Monkeys.
 - Removed Double Kick on Cubone so it's more inline with its peers power-wise.

Bug Fixes:

 - Fixed the Ranch Egg gift giving out undocumented Pokémon and missing some documented Pokémon.
 - Fixed Roxie incorrectly calling the player 'Testing', regardless of your actual name.
 - Fixed the incorrect positioning of trainers on Route 20. (Both this and the next change were caused by the same thing!).
 - Fixed an issue where completing the Pokéstar tutorial then fighting the Virbank grunts will crash the game. The player now only has access to Pokéstar Studios after beating Elesa, effectively solving the problem.
 - Changed Wave Crash's animation so that your Pokémon doesn't disappear for the rest of the fight after using the move.
 - Fixed the documentation for Route 4's fishing encounters.
 - Fixed the documents which had incorrect Feebas odds in Aspertia city.
 - Fixed Disarming Voice so it now hits both opponents.
 - Fixed Machop accidentally learning Bullet Seed, over Bullet Punch.
 - Fixed Simisear accidentally learning Lava Plume, over Flame Burst.
 - Fixed Pignite and Emboar accidentally learning Mud Bomb, over Mud Shot.
 - Marowak now correctly learns Flare Blitz.
 - Fixed Sneasel's abilities being the wrong away around, leading to confusion. Sneasel and Weavile's abilities now line up correctly.
 - Fixed Present generally being a bit broken.
 - Fixed (hopefully!) Psychic Fangs not correctly breaking screens.
 - Fixed the Blaze Black 2 version of Redux not containing the correct start-up screen.
 - Fixed Sunkern's first ability slot being incorrectly listed as Early Bird.
 - Fixed the Unovan starters being Gender and Shiny Locked. Shiny-Lockes rejoice!
 
Documentation Changes:

 - Updated the Gift Pokémon document to include the Unovan starters.
 - Updated the Important NPCs document to include the EV/Level trainers.
 - Updated the Important NPCs document to include the Audino trainer in Floccesy Ranch.
 - Updated the Pokémon Changes document to explicitly mention that the Elemental Monkeys have a different growth rate compared to vanilla.
 - Added the Infestation '----' bug to the Known Bugs document.
 - Updated the Known Issues and Hardware Information document to list some of the setups Redux is reported to work on.
 - Updated all the documents to v1.0.1.
 - Fixed Humilau City wild documentation.
 - Added the Evolution Changes document.

Other:

 - Added a version indicator to the Hall of Fame.

---

### v1.0.0 (26/03/22)

Launch version of Redux.
 
 - Various changes and corrections to documents, based on public feedback. Thanks everyone!