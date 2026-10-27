        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["glucose_mg_dl"] = pd.to_numeric(df["glucose_mg_dl"], errors="coerce")
    df = df.dropna(subset=["timestamp", "glucose_mg_dl"]).sort_values("timestamp")

    if df.empty:
        raise ValueError("No valid timestamp and glucose readings were found.")

    glucose = df["glucose_mg_dl"]

    print("BLOOD GLUCOSE LEVEL ANALYSIS")
    print("-" * 32)
    print(f"Valid readings: {glucose.count()}")
    print(f"Mean: {glucose.mean():.2f} mg/dL")
    print(f"Minimum: {glucose.min():.2f} mg/dL")
    print(f"Maximum: {glucose.max():.2f} mg/dL")
    print(f"Standard deviation: {glucose.std():.2f} mg/dL")

    print("\nAverage reading by meal timing (mg/dL):")
    print(
        df.groupby("meal_timing")["glucose_mg_dl"]
        .mean()
        .round(2)
        .to_string()
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    plt.plot(
        df["timestamp"],
        df["glucose_mg_dl"],
        marker="o",
        linewidth=1.5,
    )
    plt.title("Illustrative Blood Glucose Readings Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Glucose (mg/dL)")
    plt.xticks(rotation=35, ha="right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()

    print(f"\nChart saved to: {CHART_FILE}")
    print(
        "\nNote: The included dataset is synthetic and for learning only. "
        "This program is not a medical diagnostic tool."
    )


if __name__ == "__main__":
    main()
