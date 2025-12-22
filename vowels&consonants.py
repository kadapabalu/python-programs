text=input("Enter a string:")
vowels=0
consonants=0
vowel_letters="aeiouAEIOU"
for char in text:
    if char.isalpha():
        if char in vowel_letters:
            vowels+=1
        else:
            consonants+=1
print("number of vowles:",vowels)
print("number of consonants:",consonants)
