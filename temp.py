import pikepdf

pdf = pikepdf.open("input.pdf")

def save_pages(pdf, outname, pages):
    new = pikepdf.Pdf.new()
    for p in pages:
        new.pages.append(pdf.pages[p])
    new.save(outname)

save_pages(pdf, "part1.pdf", range(0, 5))   # 第1-5页
save_pages(pdf, "part2.pdf", range(5, 10))  # 第6-10页
