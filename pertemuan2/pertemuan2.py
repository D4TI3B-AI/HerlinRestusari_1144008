graph = {
             'Poltekpos': ['Sarijadi'],
             'Sarijadi': ['Jalan Gegerkalong'],
             'Jalan Gegerkalong': ['Jalan Setiabudi'],
             'Jalan Setiabudi': ['Jalan Cihampelas'],
             'Jalan Cihampelas': ['Ciwalk'],

        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Poltekpos sampai Ciwalk")
print("(Poltekpos, Sarijadi, Jalan Gegerkalong)")
print("(Jalan Setiabudi, Jalan Cihampelas, Ciwalk)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil
