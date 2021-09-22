import re
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

def update_views(req, obj):
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(obj)
    hits = hit_count.hits
    hitcontext = context["hitcount"] = {"pk": hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(req, hit_count)


    if hit_count_response.hit_counted:
        hits += 1
        hitcontext["hitcounted"] = hit_count_response.hit_counted
        hitcontext["hit_message"] = hit_count_response.hit_message
        hitcontext["total_hits"] = hits