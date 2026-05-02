def harflar_soni(matn):
    harflar = {}
    for harf in matn.lower():
        if harf.isalpha():
            if harf in harflar:
                harflar[harf] += 1
            else:
                harflar[harf] = 1
    return harflar

matn = input("Matnni kiriting: ")
print(harflar_soni(matn))
```

```python
def harflar_soni(matn):
    harflar = {}
    for harf in matn.lower():
        if harf.isalpha():
            harflar[harf] = harflar.get(harf, 0) + 1
    return harflar

matn = "Hello, World!"
print(harflar_soni(matn))
