"""Implementasi priority queue dan algoritma Dijkstra untuk pencarian jalur terpendek."""


class PriorityQueue:
    """Antrian prioritas sederhana berbasis heap minimum."""

    def __init__(self):
        """Inisialisasi heap kosong untuk menyimpan elemen."""
        self.heap = []

    def is_empty(self):
        """Mengembalikan True jika antrian kosong."""
        return len(self.heap) == 0

    def push(self, item):
        """Tambahkan item ke antrian dan perbaiki susunan heap."""
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        """Keluarkan item dengan prioritas terkecil dari heap."""
        if self.is_empty():
            return None

        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            min_val = self.heap.pop()
            self._bubble_down(0)
            return min_val
        else:
            return self.heap.pop()

    def _bubble_up(self, index):
        """Pindahkan elemen ke atas selama lebih kecil dari parent-nya."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _bubble_down(self, index):
        """Pindahkan elemen ke bawah untuk menjaga sifat heap minimum."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def _swap(self, i, j):
        """Tukar dua elemen pada indeks yang diberikan."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def dijkstra(graph, start, end):
    """Hitung jalur terpendek dari start ke end menggunakan algoritma Dijkstra.

    Args:
        graph: Peta graf berbentuk dictionary dengan node sebagai kunci dan
            neighbor beserta bobot sebagai nilai.
        start: Node awal.
        end: Node tujuan.

    Returns:
        Tuple berisi jalur (list) dan jarak total. Jika jalur tidak ada,
        mengembalikan (None, infinity).
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    pq = PriorityQueue()
    pq.push((0, start))

    previous_nodes = {node: None for node in graph}

    while not pq.is_empty():
        current_distance, current_node = pq.pop()

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                pq.push((distance, neighbor))

    path = []
    current = end
    if distances[end] == float('infinity'):
        return None, float('infinity')

    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[end]