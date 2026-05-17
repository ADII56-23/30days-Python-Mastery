# Mini Voting System
candidates = ["aditya", "raj", "rudra"]
votes = {candidate: 0 for candidate in candidates}
print("Candidates are:", ", ".join(candidates))
num_voters = int(input("Enter number of voters: "))

for i in range(num_voters):
    print(f"\nVoter {i+1}, please give your vote.")
    vote = input("Enter candidate name: ").strip()

    if vote in votes:
        votes[vote] += 1
        print("Vote recorded")
    else:
        print(" Vote not counted.")

print("Results")
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")
winner = max(votes, key=votes.get)
print(f"\nWinner is: {winner}")