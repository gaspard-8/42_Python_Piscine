#!/usr/bin/env python3

def main():
    print("=== Achievement Tracker System ==")
    al_ach = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_achv = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    ch_achv = {'level_10', 'treasure_hunter', 'boss_slayer',
                           'speed_demon', 'perfectionist'}
    un_achv = set.union(al_ach, bob_achv, ch_achv)
    com_achv = set.intersection(al_ach, ch_achv, bob_achv)
    al_un = set.intersection(al_ach, set.difference(un_achv, bob_achv),
                             set.difference(un_achv, ch_achv))
    bob_un = set.intersection(bob_achv, set.difference(un_achv, al_ach),
                              set.difference(un_achv, ch_achv))
    ch_un = set.intersection(ch_achv, set.difference(un_achv, al_ach),
                             set.difference(un_achv, bob_achv))
    rare_ach = set.union(al_un, bob_un, ch_un)
    print(f"player alice achievements : {al_ach}")
    print(f"player bob achievements : {bob_achv}")
    print(f"player charlie achievements : {ch_achv}")
    print()
    print(f" ALL unique achievements : {un_achv}")
    print(f"Total unique achievements : {len(un_achv)}")
    print()
    print(f"Common to all players : {com_achv}")
    print(f"Rare achievements (1 player): {rare_ach}")
    print()
    print(f"Alice vs Bob :\n common: {set.intersection(al_ach, bob_achv)}")
    print(f"Alice unique : {set.difference(al_ach, bob_achv)}")
    print(f"Bob unique: {set.difference(bob_achv, al_ach)}")


if __name__ == "__main__":
    main()
