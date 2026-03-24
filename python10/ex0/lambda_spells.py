def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda obj: -obj["power"])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"*{x}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats = {}
    stats.update({"max_power": max(mages, key=lambda x: x['power'])["power"]})
    stats.update({"min_power": min(mages, key=lambda x: x['power'])["power"]})
    stats.update({"avg_power": sum(mage["power"] for mage in mages) /
                  len(mages)})
    return stats


def main():
    artifacts = [{'name': 'Ice Wand', 'power': 100, 'type': 'relic'}, {'name': 'Earth Shield', 'power': 117, 'type': 'weapon'}, {'name': 'Lightning Rod', 'power': 76, 'type': 'armor'}, {'name': 'Water Chalice', 'power': 111, 'type': 'armor'}]  # noqa : E501
    mages = [{'name': 'Riley', 'power': 86, 'element': 'shadow'}, {'name': 'Storm', 'power': 76, 'element': 'earth'}, {'name': 'Nova', 'power': 76, 'element': 'shadow'}, {'name': 'Rowan', 'power': 81, 'element': 'shadow'}, {'name': 'Morgan', 'power': 68, 'element': 'fire'}]  # noqa : E501
    spells = ['blizzard', 'heal', 'earthquake', 'tornado']

    print("Testing artifact sorter ...")
    sort_artif = artifact_sorter(artifacts)
    for art in sort_artif:
        print(f"{art['name']} ({art['power']} power)")
    filt_mages = power_filter(mages, 75)

    print()
    print("Testing power filter (>75)")
    for mage in filt_mages:
        print(f"{mage['name']} ({mage['power']} power)")

    print()
    print("Testing map: ")
    print(f"new spells: {spell_transformer(spells)}")
    print()

    print("Testing mage_stats:")

    print(mage_stats(mages))


if __name__ == "__main__":
    main()
