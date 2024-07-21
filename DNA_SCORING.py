import random

def create_dna(lenght):

    # kullanıcının girdiği uzunlukta DNA oluşturuldu ve stringe atıldı 
    nucleotit = ["A", "C", "G", "T"]
    dna = ""
    for i in range(lenght):
        dna = dna + nuc[random.randint(0, 3)]
    return dna

def contol_dna(dna):
    hata = 0
    hata_indisleri = ["Hatalı İndisler : "]
    for i in dna:
        if i == 'A' or i == 'C' or i == 'G' or i == 'T':
            hata = hata + 0
        else:
            hata_indisleri.append(i)
            hata = hata + 1
    if hata == 0:
        print("DNA dizilimi hatasızdır.")
        return 0
    else:
        print("DNA dizilimi HATALIDIR !")
        print(hata_indisleri)
        return 404

def reverse_complements(sekanslar, sekans_lenght):
    complements = ""
    for i in range(0, len(sekanslar), sekans_lenght):
        temp = ""
        for k in range(i, i + sekans_lenght):
            if sekanslar[k] == 'A':
                temp = temp + 'T'
            elif sekanslar[k] == 'C':
                temp = temp + 'G'
            elif sekanslar[k] == 'G':
                temp = temp + 'C'
            elif sekanslar[k] == 'T':
                temp = temp + 'A'
        complements = complements + temp[::-1]
    return complements

def scoring(matrix1, matrix2):
    scorematrix = [[0 for x in range(seq_len+1)] for y in range(seq_len+1)]

    arr_normal = ""
    arr_comp = ""
    for t in range(0,seq_len):
        for i in range(0, seq_len):
            arr_normal = matrix1[i]
            for j in range(0, seq_len):
                arr_comp = matrix2[j]
                if arr_normal[i] == arr_comp[i]:
                    scorematrix[i + 1][j + 1] = scorematrix[i][j] + match_point
                else:
                    scorematrix[i + 1][j + 1] = scorematrix[i][j] - mismatch_point


                if scorematrix[i + 1][j + 1] < 0:
                    scorematrix[i + 1][j + 1] = 0


        return scorematrix

def top_scorer(matrix):#matrixlerdeki tarama yapılarak en yüksek skor, o skorun i,j değerleri geriye döndürüldü
    max_number=matrix[0][0]
    arr=[]


    for i in range(0,seq_len):
        for j in range(0,seq_len):
            if max_number<matrix[i][j]:
                index1 = i
                index2 = j
                max_number=matrix[i][j]





    return max_number,index1,index2

def dna_sekans(dnaaa, lenght, piece):
#DNA dan rastgele paralar alındı
    dna = ""
    dna = dna + dnaaa
    border = int(len(dna)) - lenght
    temp_sekans = ""
    for i in range(piece + 1):
        selector = random.randint(0, border)
        for k in range(selector, selector + lenght):
            temp_sekans = temp_sekans + str(dna[k])
    return temp_sekans

# a=random.randint(1,4)
a = [random.randrange(1, 5) for i in range(1, dna_len + 1)]
converted_seq_list = []
for m in range(1, dna_len):#dna uzunluğu sayı olarak 1-4 arasında alındı
    if a[m - 1] == 1:
        converted_seq_list.append('A')
    elif a[m - 1] == 2:
        converted_seq_list.append('C')
    elif a[m - 1] == 3:
        converted_seq_list.append('G')
    elif a[m - 1] == 4:
        converted_seq_list.append('T')
print(a)
print(converted_seq_list)

seq_matrix = [[0 for x in range(seq_len + 1)] for y in range(seq_number)]
seq_matrix_com = [[0 for f in range(seq_len + 1)] for t in range(seq_number)]

for i in range(seq_number):#alınan dna bazlara çevrildi
    slicer = random.randrange(0, len(converted_seq_list) - seq_len)
    for j in range(0, seq_len + 1):
        seq_matrix[i][j] = converted_seq_list[slicer + j]

for i in range(seq_number):#component ve reverse işlemleri yapıldı
    for j in range(0, seq_len + 1):
        if seq_matrix[i][seq_len - j - 1] == 'A':
            seq_matrix_com[i][j] = 'T'
        elif seq_matrix[i][seq_len - j - 1] == 'C':
            seq_matrix_com[i][j] = 'G'
        elif seq_matrix[i][seq_len - j - 1] == 'G':
            seq_matrix_com[i][j] = 'C'
        elif seq_matrix[i][seq_len - j - 1] == 'T':
            seq_matrix_com[i][j] = 'A'
print("Normal Sequence")#component ve normal sekanslar batırıldı ekrana
for i in range(seq_number):
    print(seq_matrix[i])
print("Component Sequence")
for i in range(seq_number):
    print(seq_matrix_com[i])
getter_array_scores = [], []
getter_array_scores = scoring(seq_matrix_com, seq_matrix_com)
for i in range(0, seq_len):
    print(getter_array_scores[i])




general_matrix = [['' for x in range(seq_number + 1)] for y in range(seq_number +1)]
for i in range(0,seq_number):#genel skor matisi oluşturuludu
    for j in range(0,seq_number):
        if i==j:
            general_matrix[i][j]='*'


for m in range(0,seq_number):
    print(general_matrix[m])





    def main():

        lenght = int(input("DNA'nın Uzunluğunu Giriniz : "))
        a_dna = atama_dna(lenght)
        sek_lenght = int(input("Sekans Uzunluğunu Giriniz (L): "))
        sek_piece = int(input("Kaç adet sekans istiyorsunuz (N): "))
        rev_comp = reverse_complements(sek_dna, sek_lenght)
        match_point = int(input("Match puanını giriniz : "))
        missmatch_point = int(input("Miss match puanını giriniz : "))
        indell_point = int(input("Indell puanını giriniz : "))
       

       
        sonuc_matrix = overlap_matrix_for_sequence_assembly(sas_score, sarc_score, sek_piece, min_score)
        create_score_csv(sonuc_matrix, "sonuc_matrix")



main()
