import reversion
from django.contrib.contenttypes.models import ContentType
from django.db import models
from apis_core.apis_entities.models import TempEntityClass


@reversion.register(follow=["tempentityclass_ptr"])
class person(TempEntityClass):
    # auto generated from model xml
    first_name = models.CharField(max_length=1024, blank=True, null=True)
    GENDER_CHOICES = (("männlich", "männlich"), ("weiblich", "weiblich"), ("unbekannt", "unbekannt"), )
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, blank=True)
    alternative_label = models.TextField(blank=True, null=True)
    

@reversion.register(follow=["tempentityclass_ptr"])
class function(TempEntityClass):
    # auto generated from model xml
    alternative_label = models.TextField(blank=True, null=True)
    

@reversion.register(follow=["tempentityclass_ptr"])
class place(TempEntityClass):
    # auto generated from model xml
    alternative_label = models.TextField(blank=True, null=True)
    TYPE_CHOICES = (("Stadt", "Stadt"), ("Dorf", "Dorf"), ("Burg", "Burg"), ("Land/Herrschaftskomplex", "Land/Herrschaftskomplex"), ("Landschaft/Region", "Landschaft/Region"), )
    type = models.CharField(max_length=23, choices=TYPE_CHOICES, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    

@reversion.register(follow=["tempentityclass_ptr"])
class institution(TempEntityClass):
    # auto generated from model xml
    alternative_label = models.TextField(blank=True, null=True)
    TYPE_CHOICES = (("Kanzlei", "Kanzlei"), ("Hofkapelle", "Hofkapelle"), ("Küche", "Küche"), ("(Dom-)Kapitel", "(Dom-)Kapitel"), ("Universität", "Universität"), ("Kloster", "Kloster"), ("Frauenzimmer", "Frauenzimmer"), ("Bistum", "Bistum"), ("Pfarrei", "Pfarrei"), )
    type = models.CharField(max_length=13, choices=TYPE_CHOICES, blank=True)
    

@reversion.register(follow=["tempentityclass_ptr"])
class court(TempEntityClass):
    # auto generated from model xml
    alternative_label = models.TextField(blank=True, null=True)
    TYPE_CHOICES = (("Hof", "Hof"), ("Klosterhof", "Klosterhof"), ("Kaiserhof", "Kaiserhof"), ("Königshof", "Königshof"), ("Bischöflicher Hof", "Bischöflicher Hof"), ("Kurfürstlicher Hof", "Kurfürstlicher Hof"), ("Erzbischöflicher Hof", "Erzbischöflicher Hof"), ("Königlicher Hof", "Königlicher Hof"), ("Kaiserlicher Hof", "Kaiserlicher Hof"), ("Frauenzimmer", "Frauenzimmer"), )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True)
    

@reversion.register(follow=["tempentityclass_ptr"])
class event(TempEntityClass):
    # auto generated from model xml
    alternative_label = models.TextField(blank=True, null=True)
    TYPE_CHOICES = (("Hochzeit", "Hochzeit"), ("Landtag", "Landtag"), ("Fest/Turnier", "Fest/Turnier"), ("Schlacht", "Schlacht"), ("Gesandtschaft/Reise", "Gesandtschaft/Reise"), ("Taufe", "Taufe"), ("Amtseinsetzung", "Amtseinsetzung"), ("Reichstag", "Reichstag"), )
    type = models.CharField(max_length=19, choices=TYPE_CHOICES, blank=True)
    

@reversion.register(follow=["tempentityclass_ptr"])
class salary(TempEntityClass):
    # auto generated from model xml
    amount = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=1024, blank=True, null=True)
    repetitions = models.IntegerField(null=True, blank=True)
    repetition_note = models.TextField(blank=True, null=True)
    TYPE_CHOICES = (("einfach", "einfach"), ("wiederholend", "wiederholend"), )
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, blank=True)
    


def construct_properties():

    from apis_core.apis_vocabularies.models import TextType
    from apis_core.apis_metainfo.models import Collection
    from apis_core.apis_relations.models import Property
    from apis_highlighter.models import AnnotationProject, Project
    from django.contrib.auth.models import User

    
    bewohnt = Property.objects.create(
        name="bewohnt",
        name_reverse="Bewohner von",
    )
    bewohnt.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    bewohnt.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    besitzt = Property.objects.create(
        name="besitzt",
        name_reverse="Besitzer von",
    )
    besitzt.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    besitzt.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    hat_korrespondenz_mit = Property.objects.create(
        name="hat Korrespondenz mit",
        name_reverse="hat Korrespondenz mit",
    )
    hat_korrespondenz_mit.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_korrespondenz_mit.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    hat_familienbeziehung_zu = Property.objects.create(
        name="hat Familienbeziehung zu",
        name_reverse="hat Familienbeziehung zu",
    )
    hat_familienbeziehung_zu.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_familienbeziehung_zu.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_elternteil_von = Property.objects.create(
        name="ist Elternteil von",
        name_reverse="ist Kind von",
    )
    ist_elternteil_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_elternteil_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_bruder_schwester_von = Property.objects.create(
        name="ist Bruder/Schwester von",
        name_reverse="ist Bruder/Schwester von",
    )
    ist_bruder_schwester_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_bruder_schwester_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_kind_von = Property.objects.create(
        name="ist Kind von",
        name_reverse="ist Elternteil von",
    )
    ist_kind_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_kind_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    hat_ehe_mit = Property.objects.create(
        name="hat Ehe mit",
        name_reverse="hat Ehe mit",
    )
    hat_ehe_mit.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_ehe_mit.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    war_anwesend_bei = Property.objects.create(
        name="war anwesend bei",
        name_reverse="hatte anwesende Person",
    )
    war_anwesend_bei.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    war_anwesend_bei.obj_class.add(ContentType.objects.get(model=court.__name__))
    
    
    empfahl = Property.objects.create(
        name="empfahl",
        name_reverse="wurde empfohlen von",
    )
    empfahl.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    empfahl.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    hat_geschäftsbeziehung_zu = Property.objects.create(
        name="hat Geschäftsbeziehung zu",
        name_reverse="hat Geschäftsbeziehung zu",
    )
    hat_geschäftsbeziehung_zu.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_geschäftsbeziehung_zu.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    mitglied_von = Property.objects.create(
        name="Mitglied von",
        name_reverse="hatte Mitglied",
    )
    mitglied_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    mitglied_von.obj_class.add(ContentType.objects.get(model=institution.__name__))
    
    
    nahm_teil_an = Property.objects.create(
        name="nahm teil an",
        name_reverse="hatte teilnehmende Person",
    )
    nahm_teil_an.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    nahm_teil_an.obj_class.add(ContentType.objects.get(model=event.__name__))
    
    
    erhielt_gehalt = Property.objects.create(
        name="erhielt Gehalt",
        name_reverse="wurde ausbezahlt an",
    )
    erhielt_gehalt.subj_class.add(ContentType.objects.get(model=salary.__name__))
    
    erhielt_gehalt.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    weist_an = Property.objects.create(
        name="weist an",
        name_reverse="auf Anweisung von",
    )
    weist_an.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    weist_an.obj_class.add(ContentType.objects.get(model=salary.__name__))
    
    
    geboren_in = Property.objects.create(
        name="geboren in",
        name_reverse="Geburtsort von",
    )
    geboren_in.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    geboren_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    gestorben_in = Property.objects.create(
        name="gestorben in",
        name_reverse="Sterbeort von",
    )
    gestorben_in.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    gestorben_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    ist_an = Property.objects.create(
        name="ist an",
        name_reverse="hat Funktion",
    )
    ist_an.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ist_an.obj_class.add(ContentType.objects.get(model=institution.__name__))
    ist_an.obj_class.add(ContentType.objects.get(model=court.__name__))
    
    
    wird_bekleidet_von = Property.objects.create(
        name="wird bekleidet von",
        name_reverse="hat Funktion inne",
    )
    wird_bekleidet_von.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    wird_bekleidet_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ging_hervor_aus = Property.objects.create(
        name="ging hervor aus",
        name_reverse="war Vorgänger von",
    )
    ging_hervor_aus.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ging_hervor_aus.obj_class.add(ContentType.objects.get(model=function.__name__))
    
    
    ist_untergeordnet = Property.objects.create(
        name="ist untergeordnet",
        name_reverse="hat untergeordnete Funktion",
    )
    ist_untergeordnet.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ist_untergeordnet.obj_class.add(ContentType.objects.get(model=function.__name__))
    
    
    teil_von = Property.objects.create(
        name="Teil von",
        name_reverse="hat Teil",
    )
    teil_von.subj_class.add(ContentType.objects.get(model=place.__name__))
    
    teil_von.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    zahlte_aus = Property.objects.create(
        name="zahlte aus",
        name_reverse="wurde ausbezahlt von",
    )
    zahlte_aus.subj_class.add(ContentType.objects.get(model=institution.__name__))
    
    zahlte_aus.obj_class.add(ContentType.objects.get(model=salary.__name__))
    
    
    ist_gelegen_in = Property.objects.create(
        name="ist gelegen in",
        name_reverse="inkludiert",
    )
    ist_gelegen_in.subj_class.add(ContentType.objects.get(model=institution.__name__))
    
    ist_gelegen_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    fand_statt_in = Property.objects.create(
        name="fand statt in",
        name_reverse="inkludierte",
    )
    fand_statt_in.subj_class.add(ContentType.objects.get(model=event.__name__))
    
    fand_statt_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    wurde_ausbezahlt_an = Property.objects.create(
        name="wurde ausbezahlt an",
        name_reverse="erhielt",
    )
    wurde_ausbezahlt_an.subj_class.add(ContentType.objects.get(model=salary.__name__))
    
    wurde_ausbezahlt_an.obj_class.add(ContentType.objects.get(model=function.__name__))
    
    