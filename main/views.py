from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AIFramework, Item
from .forms import CreateNewFramework
from .forms import SearchChatGPT
import openai
import time

# Create your views here.
openai.api_key = "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"


def ask_question(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=10,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=1024,
    )
    response = response.choices[0].text.strip()
    return response


def index(response, id):
    ls = AIFramework.objects.get(id=id)
    if ls in response.user.aiframework.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("add"):
                txt = response.POST.get("new")
                txt1 = response.POST.get("new-1")
                print(txt)
                print(txt1)
                if len(txt) > 2:
                    ls.item_set.create(text=txt, text_desc=txt1, complete=False)
                else:
                    print("Invalid")
            elif response.POST.get("search"):
                return HttpResponseRedirect("/search")
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/home.html", {})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewFramework(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = AIFramework(name=n)
            t.save()
            response.user.aiframework.add(t)
            t.item_set.create(text="Ethics Issue No 1", text_desc="Racism", complete=False)
            t.item_set.create(text="Ethics Issue No 2", text_desc="Impact On Jobs - Is It Creating Jobs?", complete=False)
            t.item_set.create(text="Ethics Issue No 3", text_desc="Impact On Jobs - Is It Taking Away Jobs?", complete=False)
            t.item_set.create(text="Ethics Issue No 4", text_desc="Privacy", complete=False)
            t.item_set.create(text="Ethics Issue No 5", text_desc="Bias", complete=False)
            t.item_set.create(text="Ethics Issue No 6", text_desc="Discrimination", complete=False)
            t.item_set.create(text="Ethics Issue No 7", text_desc="Accountability", complete=False)
            t.item_set.create(text="Ethics Issue No 8", text_desc="Misuse - Does it have potential to be misused?", complete=False)
            t.item_set.create(text="Ethics Issue No 9", text_desc="Misuse - Could it be dangerous in the hands of the wrong people?", complete=False)

        return HttpResponseRedirect("/%i" %t.id)
        # Need to look at this to work out how to send prompts when certain buttons are used in ChatGPT mode

    else:
        form = CreateNewFramework()
    return render(response, "main/create.html", {"form":form})


def view(response):
    return render(response, "main/view.html", {})


def search(response):
    if response.method == "POST":
        print("Here")
        form = SearchChatGPT(response.POST)
        if form.is_valid():
            prompt = form.cleaned_data["searchPrompt"]
            result = ask_question(prompt)
            print(result)
            time.sleep(1)
        return render(response, "main/search.html", {'form': form, 'result': result})
    else:
        form = SearchChatGPT()
        return render(response, "main/search.html", {'form': form})



