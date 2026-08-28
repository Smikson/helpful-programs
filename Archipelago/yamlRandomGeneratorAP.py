import random

print('Setting up unit selection')

# Hold any extra starting units to add at the end based on selection
extra_units = dict()

# Terran Setup
terran_exclusion = dict()
terran_exclusion['Banshee'] = {'Dusk Wings', 'Progressive Terran Ship Upgrade'}
terran_exclusion['Battlecruiser'] = {'Jackson\'s Revenge', 'Progressive Terran Ship Upgrade'}
terran_exclusion['Cyclone'] = {'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Diamondback'] = {'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Dominion Trooper'] = {'Dominion Trooper Weapons Items', 'Progressive Terran Infantry Upgrade'}
terran_exclusion['Firebat'] = {'Devil Dogs', 'Medic', 'Skibi\'s Angels', 'Medic Items', 'Progressive Terran Infantry Upgrade'}
extra_units['Firebat'] = ['Medic']
terran_exclusion['Ghost'] = {'Progressive Terran Infantry Upgrade'}
terran_exclusion['Goliath'] = {'Spartan Company', 'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Hellion'] = {'Progressive Terran Vehicle Upgrade'}
terran_exclusion['HERC'] = {'Progressive Terran Infantry Upgrade', 'Medivac', 'Medivac Items', 'Progressive Terran Ship Upgrade'}
extra_units['HERC'] = ['Medivac']
terran_exclusion['Liberator'] = {'Midnight Riders', 'Progressive Terran Ship Upgrade'}
terran_exclusion['Marauder'] = {'Hammer Securities', 'Progressive Terran Infantry Upgrade'}
terran_exclusion['Marine'] = {'War Pigs', 'Progressive Terran Infantry Upgrade'}
terran_exclusion['Predator'] = {'Progressive Terran Vehicle Upgrade', 'Hercules', 'Hercules Items', 'Progressive Terran Ship Upgrade'}
extra_units['Predator'] = ['Hercules']
terran_exclusion['Raven'] = {'Science Vessel', 'Science Vessel Items', 'Progressive Terran Ship Upgrade'}
extra_units['Raven'] = ['Science Vessel']
terran_exclusion['Reaper'] = {'Death Heads', 'Progressive Terran Infantry Upgrade'}
terran_exclusion['Siege Tank'] = {'Siege Breakers', 'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Spectre'] = {'Progressive Terran Infantry Upgrade'}
terran_exclusion['Thor'] = {'Jotun', 'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Valkyrie'] = {'Brynhilds', 'Progressive Terran Ship Upgrade', 'Firebat', 'Firebat Items', 'Devil Dogs', 'Progressive Terran Infantry Upgrade'}
extra_units['Valkyrie'] = ['Firebat']
terran_exclusion['Viking'] = {'Hel\'s Angels', 'Progressive Terran Ship Upgrade'}
terran_exclusion['Vulture'] = {'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Warhound'] = {'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Widow Mine'] = {'Progressive Terran Vehicle Upgrade'}
terran_exclusion['Wraith'] = {'Winged Nightmares', 'Progressive Terran Ship Upgrade'}

# Zerg Setup
zerg_exclusion = dict()
zerg_exclusion['Aberration'] = {'Defiler', 'Defiler Items', 'Progressive Zerg Ground Upgrade'}
extra_units['Aberration'] = ['Defiler']
zerg_exclusion['Baneling'] = {'Scourge', 'Scourge Items', 'Progressive Zerg Ground Upgrade'}
extra_units['Baneling'] = ['Scourge']
zerg_exclusion['Corruptor'] = {'Brood Lord', 'Brood Lord Items', 'Progressive Zerg Flyer Upgrade'}
extra_units['Corruptor'] = ['Brood Lord']
zerg_exclusion['Guardian'] = {'Devourer', 'Devourer Items', 'Progressive Zerg Flyer Upgrade'}
extra_units['Guardian'] = ['Devourer']
zerg_exclusion['Hydralisk'] = {'Hunter Killers', 'Progressive Zerg Ground Upgrade'}
zerg_exclusion['Infested Banshee'] = {'Infested Missile Turret', 'Infested Missile Turret Items', 'Infested Dusk Wings', 'Progressive Zerg Flyer Upgrade'}
extra_units['Infested Banshee'] = ['Infested Missile Turret']
zerg_exclusion['Infested Diamondback'] = {'Infested Missile Turret', 'Infested Missile Turret Items', 'Bullfrog', 'Bullfrog Items', 'Progressive Zerg Ground Upgrade'}
extra_units['Infested Diamondback'] = ['Infested Missile Turret', 'Bullfrog']
zerg_exclusion['Infested Liberator'] = {'Infested Missile Turret', 'Infested Missile Turret Items', 'Progressive Zerg Flyer Upgrade'}
extra_units['Infested Liberator'] = ['Infested Missile Turret']
zerg_exclusion['Infested Marine'] = {'Infested Missile Turret', 'Infested Missile Turret Items', 'Infested Bunker', 'Infested Bunker Items', 'Hunterling', 'Infested Medics', 'Progressive Zerg Ground Upgrade'}
extra_units['Infested Marine'] = ['Infested Missile Turret', 'Infested Bunker']
zerg_exclusion['Infested Siege Tank'] = {'Infested Missile Turret', 'Infested Missile Turret Items', 'Infested Siege Breakers', 'Progressive Zerg Ground Upgrade'}
extra_units['Infested Siege Tank'] = ['Infested Missile Turret']
zerg_exclusion['Infestor'] = {'Progressive Zerg Ground Upgrade', 'Progressive Zerg Flyer Upgrade'}
zerg_exclusion['Lurker'] = {'Impaler', 'Impaler Items', 'Progressive Zerg Ground Upgrade'}
extra_units['Lurker'] = ['Impaler']
zerg_exclusion['Mutalisk'] = {'Progressive Zerg Flyer Upgrade'}
zerg_exclusion['Pygalisk'] = {'Progressive Zerg Ground Upgrade'}
zerg_exclusion['Ravager'] = {'Primal Igniter', 'Primal Igniter Items', 'Progressive Zerg Ground Upgrade'}
extra_units['Ravager'] = ['Primal Igniter']
zerg_exclusion['Roach'] = {'Caustic Horrors', 'Viper', 'Viper Items', 'Progressive Zerg Ground Upgrade', 'Progressive Zerg Flyer Upgrade'}
zerg_exclusion['Roach'] = ['Viper']
zerg_exclusion['Swarm Host'] = {'Progressive Zerg Ground Upgrade'}
zerg_exclusion['Swarm Queen'] = {'Brood Queen', 'Brood Queen Items', 'Progressive Zerg Ground Upgrade'}
extra_units['Swarm Queen'] = ['Brood Queen']
zerg_exclusion['Tyrannozor'] = {'Progressive Zerg Ground Upgrade'}
zerg_exclusion['Ultralisk'] = {'Wise Old Torrasque', 'Progressive Zerg Ground Upgrade'}
zerg_exclusion['Zergling'] = {'Devouring Ones', 'Progressive Zerg Ground Upgrade'}

# Protoss Setup
protoss_exclusion = dict()
random_actual_selection = dict() # Maps base selection with same upgrades to the varients (ex: {Zealot: [Zealot, Centurian, Sentinel]})
protoss_exclusion['Adept'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Ascendant'] = {'Supplicant', 'Supplicant Items', 'Progressive Protoss Ground Upgrade'}
extra_units['Ascendant'] = ['Supplicant']
protoss_exclusion['Carrier'] = {'Carrier Class Items', 'Carrier | Trireme Items', 'Progressive Protoss Air Upgrade'}
random_actual_selection['Carrier'] = ['Carrier', 'Trireme', 'Skylord']
protoss_exclusion['Colossus'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Corsair'] = {'Oracle', 'Oracle Items', 'Progressive Protoss Air Upgrade'}
extra_units['Corsair'] = ['Oracle']
protoss_exclusion['Dark Archon'] = {'Dark Archon Meld', 'Dark Archon Meld (Dark Templar)', 'Indomitable Will', 'Indomitable Will (Dark Archon)', 'Feedback (Dark Archon)', 'Maelstrom', 'Maelstrom (Dark Archon)', 'Argus Talisman', 'Argus Talisman (Dark Archon)', 'Dark Templar', 'Resource Efficiency (Dark Templar/Avenger/Blood Hunter)', 'Progressive Protoss Ground Upgrade'}
extra_units['Dark Archon'] = ['Dark Archon Meld (Dark Templar)']
protoss_exclusion['Dark Templar'] = {'Dark Templar Class Items', 'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Disruptor'] = {'Progressive Protoss Ground Upgrade'}
random_actual_selection['Dark Templar'] = ['Dark Templar', 'Avenger', 'Blood Hunter']
protoss_exclusion['Dragoon'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['High Templar'] = {'Unshackled Psionic Storm', 'Unshackled Psionic Storm (High Templar/Signifier)', 'Hallucination (High Templar/Signifier)', 'Khaydarin Amulet', 'Khaydarin Amulet (High Templar/Signifier)', 'High Archon', 'High Archon (Archon)', 'Eradicate', 'Eradicate (Archon)', 'Obliterate', 'Obliterate (Archon)', 'Power Siphon', 'Power Siphon (Archon)', 'Transcendence', 'Transcendence (Archon)', 'Progressive Protoss Ground Upgrade'}
random_actual_selection['High Templar'] = ['High Templar', 'Signifier']
protoss_exclusion['Immortal'] = {'Immortal | Annihilator Items', 'Progressive Protoss Ground Upgrade'}
random_actual_selection['Immortal'] = ['Immortal', 'Annihilator']
protoss_exclusion['Phoenix'] = {'Phoenix Class Items', 'Arbiter', 'Arbiter Items', 'Progressive Protoss Air Upgrade'}
extra_units['Phoenix'] = ['Arbiter']
random_actual_selection['Phoenix'] = ['Phoenix', 'Mirage', 'Skirmisher']
protoss_exclusion['Photon Cannon'] = {'Energizer', 'Energizer Items', 'Sentry Class Items', 'Progressive Protoss Ground Upgrade'}
extra_units['Photon Cannon'] = ['Khalai Ingenuity', 'Energizer']
protoss_exclusion['Reaver'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Scout'] = {'Scout Class Items', 'Scout | Oppressor | Mist Wing Items', 'Progressive Protoss Air Upgrade'}
random_actual_selection['Scout'] = {'Scout', 'Oppressor', 'Mist Wing', 'Caladrius'}
protoss_exclusion['Stalker'] = {'Stalker Class Items', 'Progressive Protoss Ground Upgrade'}
random_actual_selection['Stalker'] = ['Stalker', 'Instigator', 'Slayer']
protoss_exclusion['Stalwart'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Tempest'] = {'Progressive Protoss Air Upgrade'}
protoss_exclusion['Vanguard'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Void Ray'] = {'Void Ray Class Items', 'Progressive Protoss Air Upgrade'}
random_actual_selection['Void Ray'] = ['Void Ray', 'Destroyer', 'Pulsar', 'Dawnbringer']
protoss_exclusion['Warp Prism'] = {'Havoc', 'Havoc Items', 'Sentry Class Items', 'Mothership', 'Mothership Items', 'Progressive Protoss Ground Upgrade', 'Progressive Protoss Air Upgrade'}
extra_units['Warp Prism'] = ['Havoc', 'Phase Blaster (Warp Prism)']
protoss_exclusion['Wrathwalker'] = {'Progressive Protoss Ground Upgrade'}
protoss_exclusion['Zealot'] = {'Zealot | Sentinel | Centurion Items', 'Sentry', 'Sentry Items', 'Sentry Class Items', 'Progressive Protoss Ground Upgrade'}
extra_units['Zealot'] = ['Sentry']
random_actual_selection['Zealot'] = ['Zealot', 'Centurion', 'Sentinel']

# Random selection, first choose race/template file, then unit
race_selection = random.choice([('TerranTemplate.txt', terran_exclusion), ('ZergTemplate.txt', zerg_exclusion), ('ProtossTemplate.txt', protoss_exclusion)])
selection = random.choice(list(race_selection[1].keys()))
actual_selection = selection
if selection in random_actual_selection:
    actual_selection = random.choice(random_actual_selection[selection])
print('Selected Unit: ' + actual_selection)

# Read template file
print('Reading template file')
template_file = open(race_selection[0], 'r')
template_lines = template_file.readlines()
template_file.close()

# Create output lines
print('Creating output')
selection_exclusion = race_selection[1][selection]
selection_exclusion.add(actual_selection)
selection_exclusion.add(actual_selection + ' Items')
output_lines = []
for line in template_lines:
    check_line = line.strip()
    if check_line[:-3] not in selection_exclusion:
        output_lines.append(line)
    # Check for extra line
    if check_line == 'start_inventory:':
        output_lines.append('    ' + actual_selection + ': 1\n')
        if selection in extra_units:
            for unit in extra_units[selection]:
                output_lines.append('    ' + unit + ': 1\n')

# Write to output file
print('Writing output file. Don\'t forget to change the file name and the name in the file!')
output_file = open('CHANGE_NAME.yaml', 'w')
output_file.writelines(output_lines)
output_file.close()
print('Completed!')
