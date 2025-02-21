#tugas uas 
#class Node:
    def __init__(self, pertanyaan, cabang_ya=None, cabang_tidak=None):
        self.pertanyaan = pertanyaan
        self.cabang_ya = cabang_ya
        self.cabang_tidak = cabang_tidak

def diagnosa(node):
    if node.cabang_ya is None and node.cabang_tidak is None:
        print(f"Kemungkinan penyakit Anda: {node.pertanyaan}")
        return
    
    jawaban = input(f"{node.pertanyaan} (ya/tidak): ").strip().lower()
    if jawaban == 'ya':
        diagnosa(node.cabang_ya)
    else:
        diagnosa(node.cabang_tidak)

akar = Node(
    "Apakah Anda mengalami demam?",
    cabang_ya=Node(
        "Apakah Anda mengalami batuk?",
        cabang_ya=Node("Kemungkinan Anda mengalami flu."),
        cabang_tidak=Node("Kemungkinan Anda mengalami infeksi ringan.")
    ),
    cabang_tidak=Node(
        "Apakah Anda mengalami sakit perut?",
        cabang_ya=Node("Kemungkinan Anda mengalami gangguan pencernaan."),
        cabang_tidak=Node("Gejala tidak mengarah pada penyakit tertentu. Silakan konsultasi dokter.")
    )
)

diagnosa(akar)
