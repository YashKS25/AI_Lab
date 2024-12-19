def forward_reasoning_algorithm():
    print("=== Forward Reasoning Algorithm ===")
    print("Enter the knowledge base (rules and facts), one per line.")
    print("Rules should be in the format: premise1 AND premise2 => conclusion")
    print("Facts should be entered as standalone atomic sentences.")
    print("Enter 'END' to finish entering the knowledge base.\n")

    # Initialize the knowledge base and facts
    knowledge_base = []
    facts = set()

    # Input: Knowledge base (rules and facts)
    while True:
        line = input("Enter rule or fact: ").strip()
        if line.upper() == "END":
            break
        if "=>" in line:  # Rule with premises and conclusion
            premises, conclusion = line.split(" => ")
            knowledge_base.append((premises.split(" AND "), conclusion.strip()))
        else:  # Fact
            facts.add(line.strip())

    print("\n=== Knowledge Base and Initial Facts ===")
    print("Rules:")
    for premises, conclusion in knowledge_base:
        print(f"  {' AND '.join(premises)} => {conclusion}")
    print("Facts:")
    for fact in facts:
        print(f"  {fact}")
    print()

    # Input: Query
    query = input("Enter the query (atomic sentence): ").strip()
    print("\n=== Forward Reasoning Process ===")

    # Forward-chaining algorithm
    inferred = set()  # Store all inferred facts
    new_inferences = True

    while new_inferences:
        new_inferences = False
        for premises, conclusion in knowledge_base:
            # Check if all premises are satisfied in the current set of facts
            if all(p in facts for p in premises) and conclusion not in facts:
                # Infer the conclusion
                facts.add(conclusion)
                inferred.add(conclusion)
                print(f"Inferred: {conclusion}")
                new_inferences = True

    # Check if the query can be inferred
    print("\n=== Query Result ===")
    if query in facts:
        print(f"The query '{query}' is satisfied: YES")
    else:
        print(f"The query '{query}' is not satisfied: NO")
    print("=== End of Process ===")


# Run the algorithm
forward_reasoning_algorithm()
