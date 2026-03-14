import importlib as iml


def main():
    print("LOADING STATUS: Loading program...")
    print("Checking dependencies:")
    try:
        panda = iml.import_module("pandas")
        print(f"[OK] pandas ({panda.__version__})- Data manipulation ready")
        requests = iml.import_module("requests")
        print(f"[OK] requests ({requests.__version__})- Network access ready")
        numpy = iml.import_module("numpy")
        print(f"[OK] numpy ({numpy.__version__})- MATH ready")
        plotlib = iml.import_module("matplotlib")
        plt = iml.import_module("matplotlib.pyplot")
        print(f"[OK] matplotlib ({plotlib.__version__})- Visualization ready")
    except Exception as e:
        print(e)
        print("Can't analyze Data, please install first the missing "
              "dependencies using pip or poetry")
        return
    print()
    print("Getting data from open meteo")
    latitude = input("Enter your favorite latitude (-90 to 90) :")
    longitude = input("Enter your favorite longitude (-90 to 90) :")
    if (int(latitude) > 90 or int(latitude) < -90 or
            int(longitude) < -90 or int(longitude) > 90):
        print("ERROR : invalid latitude/longitude")
        return

    api_meteo = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max&timezone=Europe/Paris"  # noqa: E501
    data = requests.get(api_meteo).json()
    df = panda.DataFrame(data['daily'])
    time = df['time']
    fig, ax = plt.subplots()
    ax.set_title(f"Meteo wherever you said ({latitude} - {longitude})")

    temp_max = df['temperature_2m_max'].max()
    temp_mean = df['temperature_2m_max'].mean()

    ax.axhline(y=temp_mean, linestyle='--')
    ax.axhline(y=temp_max, linestyle=':')

    ax.plot([day[5:] for day in time], df['temperature_2m_max'])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x}°C"))
    plt.savefig("meteo.png")

    print()
    print("Weather forecast succesfullly saved to meteo.png !")


if __name__ == "__main__":
    main()
