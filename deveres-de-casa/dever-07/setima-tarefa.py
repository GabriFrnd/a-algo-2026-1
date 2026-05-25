'''
Hospital Triage System — Max-Heap Priority Queue.
Simulates ER patient prioritization by pain level (1-10).

Complexity summary:

    1. insert(): O(log n).
    2. attend_next(): O(log n).

    3. update_priority(): O(log n) — O(1) lookup via index map.
    4. peek(): O(1).
'''
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

# Patient data
@dataclass
class Patient:
    '''
    Holds a patient's triage data.
    Attributes:

        pid: Unique patient ID.
        name: Patient name.
        pain: Pain level on a 1-10 scale.
        arrival: Arrival order; breaks ties (lower = higher priority).
    '''
    pid: int
    name: str
    pain: int
    arrival: int = field(default=0)

    def __post_init__(self) -> None:
        if not (1 <= self.pain <= 10):
            raise ValueError(f'Pain must be 1-10, got {self.pain}.')

    def __repr__(self) -> str:
        return f'Patient(id={self.pid}, name={self.name!r}, pain={self.pain})'

# Max-Heap triage queue
class TriageQueue:
    '''
    Max-Heap priority queue for ER triage.
    Ordering key: (pain DESC, arrival ASC).
    An index map (pid -> heap position) keeps update_priority at O(log n).
    '''

    def __init__(self) -> None:
        self._heap: list[Patient] = []
        self._pos:  dict[int, int] = {}  # pid -> current heap index

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        # Returns True when no patients are waiting.
        return not self._heap

    def peek(self) -> Optional[Patient]:
        '''
        Returns the highest-priority patient without removing them.
        Returns:
            Top Patient, or None if the queue is empty.

        Complexity: O(1).
        '''
        return self._heap[0] if self._heap else None

    def insert(self, patient: Patient) -> None:
        '''
        Adds a patient and restores the heap property.
        Args:
            patient: Patient to enqueue.

        Complexity: O(log n).
        '''
        self._heap.append(patient)
        idx = len(self._heap) - 1

        self._pos[patient.pid] = idx
        self._sift_up(idx)

    def attend_next(self) -> Patient:
        '''
        Removes and returns the highest-priority patient.
        Returns:
            The Patient with the greatest pain (earliest arrival on tie).

        Raises:
            IndexError: If the queue is empty.

        Complexity: O(log n).
        '''
        if self.is_empty():
            raise IndexError('Queue is empty.')

        root = self._heap[0]
        tail = self._heap.pop()
        del self._pos[root.pid]

        if self._heap:
            self._heap[0] = tail
            self._pos[tail.pid] = 0
            self._sift_down(0)

        return root

    def update_priority(self, pid: int, new_pain: int) -> None:
        '''
        Updates a patient's pain level and rebalances the heap.
        Covers both Increase-Key (new_pain > old) and Decrease-Key (new_pain < old).

        Args:
            pid: ID of the patient to update.
            new_pain: Revised pain level (1-10).

        Raises:
            KeyError:   If pid is not in the queue.
            ValueError: If new_pain is outside 1-10.

        Complexity: O(log n) — O(1) lookup + O(log n) rebalance.
        '''
        if not (1 <= new_pain <= 10):
            raise ValueError(f'Pain must be 1–10, got {new_pain}.')

        if pid not in self._pos:
            raise KeyError(f'Patient id={pid} not found.')

        idx = self._pos[pid]
        old_pain = self._heap[idx].pain
        self._heap[idx].pain = new_pain

        if new_pain > old_pain: self._sift_up(idx)
        elif new_pain < old_pain: self._sift_down(idx)

    @staticmethod
    def _key(p: Patient) -> tuple[int, int]:
        # Comparison key: higher pain first; lower arrival index breaks ties.
        return (p.pain, -p.arrival)

    def _swap(self, a: int, b: int) -> None:
        # Swaps two heap positions and updates the index map
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]
        self._pos[self._heap[a].pid] = a
        self._pos[self._heap[b].pid] = b

    def _sift_up(self, i: int) -> None:
        #Bubbles node i up until the heap property holds. O(log n).
        while i > 0:
            parent = (i - 1) // 2

            if self._key(self._heap[i]) > self._key(self._heap[parent]):
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        # Pushes node i down until the heap property holds. O(log n
        n = len(self._heap)

        while True:
            largest, l, r = i, 2*i+1, 2*i+2

            if l < n and self._key(self._heap[l]) > self._key(self._heap[largest]):
                largest = l

            if r < n and self._key(self._heap[r]) > self._key(self._heap[largest]):
                largest = r

            if largest == i:
                break

            self._swap(i, largest)
            i = largest
# Demo
def main() -> None:
    # Runs a full triage simulation with insert, update, and attend calls
    print('=' * 50)
    print('  ER TRIAGE — Max-Heap Priority Queue')

    print('=' * 50)
    queue = TriageQueue()

    # Admission
    print('\n[1] Admitting patients:')
    roster: list[tuple[str, int]] = [
        ('Ana', 4), ('Bruno', 9), ('Carla', 2),
        ('Daniel', 7), ('Eduarda', 9), ('Felipe', 5),
    ]

    for seq, (name, pain) in enumerate(roster, start=1):
        p = Patient(pid=seq, name=name, pain=pain, arrival=seq)
        queue.insert(p)
        print(f'   + {p}')

    print(f'\n   Next: {queue.peek()}')

    # Priority updates
    print('\n[2] Priority updates:')

    queue.update_priority(pid=3, new_pain=10) # Carla worsened
    print(f'   Carla pain -> 10  |  Next: {queue.peek()}')

    queue.update_priority(pid=2, new_pain=3) # Bruno improved
    print(f'   Bruno pain ->  3  |  Next: {queue.peek()}')

    # Attend all
    print('\n[3] Attending in priority order:')
    order = 1

    while not queue.is_empty():
        print(f'   {order:>2}. {queue.attend_next()}')
        order += 1

if __name__ == '__main__':
    main()