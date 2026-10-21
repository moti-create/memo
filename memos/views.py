from django.shortcuts import render, redirect
from .models import Category, Memo


def home(request):
    if request.method == "POST":
        name = request.POST.get("category_name")

        if name:
            Category.objects.create(name=name)

        return redirect("home")

    categories = Category.objects.all()
    return render(request, "memos/home.html", {
        "categories": categories
    })


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == "POST":
        content = request.POST.get("content","").strip()

        if content:
            Memo.objects.create(
                category=category,
                content=content
            )

        return redirect("category_detail", category_id=category.id)

    # このカテゴリーのメモを取得
    memos = category.memo_set.all().order_by("id")

    # 検索キーワードを取得
    keyword = request.GET.get("q", "")

    # キーワードが入力されていれば、内容で検索
    if keyword:
        memos = memos.filter(content__icontains=keyword)

    return render(request, "memos/category_detail.html", {
        "category": category,
        "memos": memos,
        "keyword": keyword
    })


def delete_category(request, category_id):
    if request.method == "POST":
        category = Category.objects.get(id=category_id)
        category.delete()

    return redirect("home")


def delete_memo(request, category_id, memo_id):
    if request.method == "POST":
        memo = Memo.objects.get(
            id=memo_id,
            category_id=category_id
        )
        memo.delete()

    return redirect("category_detail", category_id=category_id)


def delete_selected_memos(request, category_id):
    if request.method == "POST":
        memo_ids = request.POST.getlist("memo_ids")

        Memo.objects.filter(
            id__in=memo_ids,
            category_id=category_id
        ).delete()

    return redirect("category_detail", category_id=category_id)
