import importlib as iml
import matplotlib.pyplot as plt

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
        print(f"[OK] matplotlib ({plotlib.__version__})- Visualization ready")
    except Exception as e:
        print(e)
        return

    print("Getting data from open meteo")
    latitude = input("Enter your favorite latitude: (-90 to 90)")
    longitude = input("Enter your favorite longitude: (-90 to 90)")
    api_meteo = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max&timezone=Europe/Paris"  # noqa: E501
    data = requests.get(api_meteo).json
    panda_data = panda.DataFrame(data)
    print(panda_data)
    time = data["daily"]["time"]
    print(time)
    temperatures = data["daily"]["temperature_2m_max"]
    print(temperatures)

    myvar = panda.Series(temperatures, index = time)

    fig, ax = plt.subplots()
    ax.set_title(f"Meteo wherever you said ({latitude} - {longitude})")
    ax.plot(time, temperatures)  # Plot some data on the Axes.
    plt.show()


if __name__ == "__main__":
    main()
