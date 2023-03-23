items = Post.objects.all() 
for item in items:
    item.title = f"{slugify(item.title)}-{item.pk}"
    item.save()
