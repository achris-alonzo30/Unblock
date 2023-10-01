from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DraftForm
from .models import Draft


def home(request):
    draft_form = DraftForm()
    drafts_per_page = 8  # Set the number of drafts per page

    if request.method == 'POST':
        draft_form = DraftForm(request.POST)

        if draft_form.is_valid():
            title = draft_form.cleaned_data['title']
            content = draft_form.cleaned_data['content']
            button_clicked = request.POST.get('button_clicked', '')

            if button_clicked == 'downloadButton':
                response = HttpResponse(content_type = 'text/plain')
                response['Content-Disposition'] = f'attachment; filename="{title}.txt"'
                response.write(content)

                # Save the draft as 'downloaded' in the database
                draft = Draft(title = title, content = content, status = 'downloaded')
                draft.save()

                return response

            elif button_clicked == 'backButton':
                if not title and not content:
                    return redirect('writingapp:home')
                else:
                    draft = Draft(title = title, content = content, status = 'drafted')
                    draft.save()
                    return redirect('writingapp:home')

    drafted_drafts = Draft.objects.filter(status = 'drafted').order_by('-created_at')
    # Paginate the drafts
    paginator = Paginator(drafted_drafts, drafts_per_page)
    page_number = request.GET.get('page')
    drafts_page = paginator.get_page(page_number)

    context = {
        'draft_form': draft_form,
        'drafts_page': drafts_page,
    }

    return render(request, 'writingapp/home.html', context)


def writing_area(request):
    draft_id = request.POST.get('draft_id')
    delete_draft_id = request.POST.get('delete_draft')  # Get the delete_draft parameter

    if delete_draft_id:  # Check if delete_draft parameter is present
        draft = get_object_or_404(Draft, id = delete_draft_id)
        draft.delete()  # Delete the draft

        return redirect('writingapp:home')

    if draft_id:
        draft = get_object_or_404(Draft, id = draft_id)
        draft_form = DraftForm(instance = draft)

    else:
        draft_form = DraftForm()

    return render(request, 'writingapp/writing_area.html', {'draft_form': draft_form})
