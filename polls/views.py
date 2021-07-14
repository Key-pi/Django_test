from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic


from .forms import PersonForm, TriangleForm
from .models import Board, Choice, Person, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class CreateBoardView(generic.CreateView):
    pass


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def triangle(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            size_a = form.cleaned_data['size_a']
            size_b = form.cleaned_data['size_b']
            result = (size_a ** 2 + size_b ** 2) ** 0.5
            return render(request, 'polls/triangle.html', context={"result": result, })
    else:
        form = TriangleForm()
    return render(request, 'polls/triangle.html', context={"form": form, })


def person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            try:
                person = form.save()
                messages.add_message(request, messages.SUCCESS, 'Person successfully added')
            except ValueError:
                messages.add_message(request, messages.ERROR, 'Person dont created')
            return redirect('polls:person_update', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'polls/person.html', context={"form": form, })


def person_update(request, pk):
    item = get_object_or_404(Person, pk=pk)
    if request.method == "GET":
        form = PersonForm(instance=item)
    else:
        form = PersonForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Person update')
            except ValueError:
                messages.add_message(request, messages.ERROR, 'Person dont update')
            return redirect('polls:person_update', pk=pk)
    return render(request, 'polls/person_update.html', context={"form": form, 'person_inst': item})


class BoardListView(generic.ListView):
    model = Board
    template_name = 'polls/board_index.html'
    context_object_name = 'board'
    paginate_by = 5


class BoardInfoView(generic.DetailView):
    model = Board
    pk_url_kwarg = 'pk'
    template_name = 'polls/board_info.html'
    context_object_name = 'board'


class BoardUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Board
    fields = ('name', 'description')
    template_name = 'polls/board_update.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'board'
    success_url = reverse_lazy('polls:board_view')


class BoardDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Board
    template_name = 'polls/board_delete.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'board'
    success_url = reverse_lazy('polls:board_view')


class BoardCreate(generic.CreateView):
    model = Board
    fields = ['name', 'description']
    template_name = 'polls/board_create.html'
    success_url = reverse_lazy('polls:board_view')
