def tower_of_hanoi(n, source_peg, auxiliary_peg, target_peg):
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
        return
    tower_of_hanoi(n-1, source_peg, target_peg, auxiliary_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    tower_of_hanoi(n-1, auxiliary_peg, source_peg, target_peg)
