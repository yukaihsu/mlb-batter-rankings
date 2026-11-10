from core_batters import load_batters, rank_batters, progress_table

def main():

    batters = load_batters("batter_state.csv")
    while True:
        print("MLB 2025 seaon batter analysis")
        print("[1] Batter Ranking")
        print("[2] Batter 2025 Performance")
        choice = input("Please select the funtion (1 or 2)").strip()

        if choice == "1":
            metric = (input("Enter metric (OPS/AVG/OBP/SLG): ").strip().upper() or "OPS")
            top_n = int(input("Show top how many players?: ") or 10)
            leaders, _ = rank_batters(batters, metric, top_n)

            print(f"\n Top Batters by {metric}\n")
            for i, b in enumerate(leaders, 1):
                value = {"AVG": b.avg(), "OBP": b.obp(), "SLG": b.slg(), "OPS": b.ops()}[metric]
                print(f"#{i:2}  {b.Name:10} {b.Team:10} {metric}:{value:.3f}")
            
            if not leaders:
                print("Invalid metric. Please enter OPS, AVG, OBP,or SLG.")
                input("\nPress Enter to return to the main menu...") 
                continue
    
        elif choice == "2":
            metric = (input("Enter metric for comparison (OPS/AVG/OBP/SLG): ").strip().upper() or "OPS")
            while metric not in {"OPS", "AVG", "OBP","SLG"}:
                print("Not valid. Please try again.")
                metric = (input("Enter metric for comparison (OPS/AVG/OBP/SLG): ").strip().upper() or "OPS")
                continue
            improved, regressed, tied= progress_table(batters, metric)
            print(f"\nImprovement List by {metric}\n")
            for i, (b, pos, delta) in enumerate(improved[:100], 1):
                print(f"#{i:2}  {b.Name:20} Pre:{b.Rank_preseason:3} → Now:{pos:3}  delta:{delta:+d}")
        
            print(f"\nDecline List by {metric}\n")
            for i, (b, pos, delta) in enumerate(regressed[:100], 1):
                print(f"#{i:2}  {b.Name:20} Pre:{b.Rank_preseason:3} → Now:{pos:3}  delta:{delta:+d}")
        
            print(f"\n Tied List\n")
            for i, (b, pos, delta) in enumerate(tied[:100], 1):
                print(f"#{i:2}  {b.Name:20} Pre:{b.Rank_preseason:3} → Now:{pos:3}  delta:{delta:+d}")
            
            input("\nPress Enter to return to the main menu...")
            continue
    
        else:
            print("No valid. Please try it again.")
            continue

if __name__ == "__main__":
    main()