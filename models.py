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
    TYPE_CHOICES = (("Stadt", "Stadt"), ("Dorf/Nachbarschaft/Gemein/Siedlung/Weiler", "Dorf/Nachbarschaft/Gemein/Siedlung/Weiler"), ("Burg/Schloss", "Burg/Schloss"), ("Land/Herrschaftskomplex", "Land/Herrschaftskomplex"), ("Landschaft/Region", "Landschaft/Region"), ("Lehen", "Lehen"), ("Haus/Hof", "Haus/Hof"), ("Gericht", "Gericht"), ("Kloster", "Kloster"), ("Gewässer", "Gewässer"), ("Grundherrschaft", "Grundherrschaft"), ("Hofmark", "Hofmark"), ("Tal", "Tal"), ("Berg", "Berg"), ("Bergrevier", "Bergrevier"), ("Pflege", "Pflege"), ("(Land-)Vogtei", "(Land-)Vogtei"), ("Propstei", "Propstei"), )
    type = models.CharField(max_length=41, choices=TYPE_CHOICES, blank=True)
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
    TYP_CHOICES = (("Sold", "Sold"), ("Zehrung", "Zehrung"), ("Provision", "Provision"), ("Kredit", "Kredit"), ("Sonstiges", "Sonstiges"), )
    typ = models.CharField(max_length=9, choices=TYP_CHOICES, blank=True)
    REPETITIONTYPE_CHOICES = (("einfach", "einfach"), ("wiederholend", "wiederholend"), )
    repetitionType = models.CharField(max_length=12, choices=REPETITIONTYPE_CHOICES, blank=True)
    


def construct_properties():

    from apis_core.apis_vocabularies.models import TextType
    from apis_core.apis_metainfo.models import Collection
    from apis_core.apis_relations.models import Property
    from apis_highlighter.models import AnnotationProject, Project
    from django.contrib.auth.models import User

    
    bewohnt = Property.objects.get_or_create(
        name="bewohnt",
        name_reverse="Bewohner von",
    )[0]
    bewohnt.subj_class.clear()
    
    bewohnt.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    bewohnt.obj_class.clear()
    
    bewohnt.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    besitzt = Property.objects.get_or_create(
        name="besitzt",
        name_reverse="Besitzer von",
    )[0]
    besitzt.subj_class.clear()
    
    besitzt.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    besitzt.obj_class.clear()
    
    besitzt.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    ist_tätig_in = Property.objects.get_or_create(
        name="ist tätig in",
        name_reverse="ist Tätigkeitsort von",
    )[0]
    ist_tätig_in.subj_class.clear()
    
    ist_tätig_in.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_tätig_in.obj_class.clear()
    
    ist_tätig_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    hält_sich_auf_in = Property.objects.get_or_create(
        name="hält sich auf in",
        name_reverse="ist Aufenthaltsort von",
    )[0]
    hält_sich_auf_in.subj_class.clear()
    
    hält_sich_auf_in.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hält_sich_auf_in.obj_class.clear()
    
    hält_sich_auf_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    hat_korrespondenz_mit = Property.objects.get_or_create(
        name="hat Korrespondenz mit",
        name_reverse="hat Korrespondenz mit",
    )[0]
    hat_korrespondenz_mit.subj_class.clear()
    
    hat_korrespondenz_mit.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_korrespondenz_mit.obj_class.clear()
    
    hat_korrespondenz_mit.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    hat_familienbeziehung_zu = Property.objects.get_or_create(
        name="hat Familienbeziehung zu",
        name_reverse="hat Familienbeziehung zu",
    )[0]
    hat_familienbeziehung_zu.subj_class.clear()
    
    hat_familienbeziehung_zu.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_familienbeziehung_zu.obj_class.clear()
    
    hat_familienbeziehung_zu.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_elternteil_von = Property.objects.get_or_create(
        name="ist Elternteil von",
        name_reverse="ist Kind von",
    )[0]
    ist_elternteil_von.subj_class.clear()
    
    ist_elternteil_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_elternteil_von.obj_class.clear()
    
    ist_elternteil_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_bruder_schwester_von = Property.objects.get_or_create(
        name="ist Bruder/Schwester von",
        name_reverse="ist Bruder/Schwester von",
    )[0]
    ist_bruder_schwester_von.subj_class.clear()
    
    ist_bruder_schwester_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_bruder_schwester_von.obj_class.clear()
    
    ist_bruder_schwester_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_kind_von = Property.objects.get_or_create(
        name="ist Kind von",
        name_reverse="ist Elternteil von",
    )[0]
    ist_kind_von.subj_class.clear()
    
    ist_kind_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_kind_von.obj_class.clear()
    
    ist_kind_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    hat_ehe_mit = Property.objects.get_or_create(
        name="hat Ehe mit",
        name_reverse="hat Ehe mit",
    )[0]
    hat_ehe_mit.subj_class.clear()
    
    hat_ehe_mit.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_ehe_mit.obj_class.clear()
    
    hat_ehe_mit.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    war_anwesend_bei = Property.objects.get_or_create(
        name="war anwesend bei",
        name_reverse="hatte anwesende Person",
    )[0]
    war_anwesend_bei.subj_class.clear()
    
    war_anwesend_bei.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    war_anwesend_bei.obj_class.clear()
    
    war_anwesend_bei.obj_class.add(ContentType.objects.get(model=court.__name__))
    
    
    empfahl = Property.objects.get_or_create(
        name="empfahl",
        name_reverse="wurde empfohlen von",
    )[0]
    empfahl.subj_class.clear()
    
    empfahl.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    empfahl.obj_class.clear()
    
    empfahl.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    hat_geschäftsbeziehung_zu = Property.objects.get_or_create(
        name="hat Geschäftsbeziehung zu",
        name_reverse="hat Geschäftsbeziehung zu",
    )[0]
    hat_geschäftsbeziehung_zu.subj_class.clear()
    
    hat_geschäftsbeziehung_zu.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    hat_geschäftsbeziehung_zu.obj_class.clear()
    
    hat_geschäftsbeziehung_zu.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ist_vormund_von = Property.objects.get_or_create(
        name="ist Vormund von",
        name_reverse="ist Mündel von",
    )[0]
    ist_vormund_von.subj_class.clear()
    
    ist_vormund_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_vormund_von.obj_class.clear()
    
    ist_vormund_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    mitglied_von = Property.objects.get_or_create(
        name="Mitglied von",
        name_reverse="hatte Mitglied",
    )[0]
    mitglied_von.subj_class.clear()
    
    mitglied_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    mitglied_von.obj_class.clear()
    
    mitglied_von.obj_class.add(ContentType.objects.get(model=institution.__name__))
    
    
    war_tätig_an = Property.objects.get_or_create(
        name="war tätig an",
        name_reverse="hatte tätige Person",
    )[0]
    war_tätig_an.subj_class.clear()
    
    war_tätig_an.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    war_tätig_an.obj_class.clear()
    
    war_tätig_an.obj_class.add(ContentType.objects.get(model=institution.__name__))
    
    
    ist_pfründner_von = Property.objects.get_or_create(
        name="ist Pfründner von",
        name_reverse="hat Pfründner",
    )[0]
    ist_pfründner_von.subj_class.clear()
    
    ist_pfründner_von.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    ist_pfründner_von.obj_class.clear()
    
    ist_pfründner_von.obj_class.add(ContentType.objects.get(model=institution.__name__))
    
    
    nahm_teil_an = Property.objects.get_or_create(
        name="nahm teil an",
        name_reverse="hatte teilnehmende Person",
    )[0]
    nahm_teil_an.subj_class.clear()
    
    nahm_teil_an.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    nahm_teil_an.obj_class.clear()
    
    nahm_teil_an.obj_class.add(ContentType.objects.get(model=event.__name__))
    
    
    erhielt_gehalt = Property.objects.get_or_create(
        name="erhielt Gehalt",
        name_reverse="wurde ausbezahlt an",
    )[0]
    erhielt_gehalt.subj_class.clear()
    
    erhielt_gehalt.subj_class.add(ContentType.objects.get(model=salary.__name__))
    
    erhielt_gehalt.obj_class.clear()
    
    erhielt_gehalt.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    weist_an = Property.objects.get_or_create(
        name="weist an",
        name_reverse="auf Anweisung von",
    )[0]
    weist_an.subj_class.clear()
    
    weist_an.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    weist_an.obj_class.clear()
    
    weist_an.obj_class.add(ContentType.objects.get(model=salary.__name__))
    
    
    geboren_in = Property.objects.get_or_create(
        name="geboren in",
        name_reverse="Geburtsort von",
    )[0]
    geboren_in.subj_class.clear()
    
    geboren_in.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    geboren_in.obj_class.clear()
    
    geboren_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    gestorben_in = Property.objects.get_or_create(
        name="gestorben in",
        name_reverse="Sterbeort von",
    )[0]
    gestorben_in.subj_class.clear()
    
    gestorben_in.subj_class.add(ContentType.objects.get(model=person.__name__))
    
    gestorben_in.obj_class.clear()
    
    gestorben_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    ist_an = Property.objects.get_or_create(
        name="ist an",
        name_reverse="hat Funktion",
    )[0]
    ist_an.subj_class.clear()
    
    ist_an.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ist_an.obj_class.clear()
    
    ist_an.obj_class.add(ContentType.objects.get(model=institution.__name__))
    
    ist_an.obj_class.add(ContentType.objects.get(model=court.__name__))
    
    
    wird_bekleidet_von = Property.objects.get_or_create(
        name="wird bekleidet von",
        name_reverse="hat Funktion inne",
    )[0]
    wird_bekleidet_von.subj_class.clear()
    
    wird_bekleidet_von.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    wird_bekleidet_von.obj_class.clear()
    
    wird_bekleidet_von.obj_class.add(ContentType.objects.get(model=person.__name__))
    
    
    ging_hervor_aus = Property.objects.get_or_create(
        name="ging hervor aus",
        name_reverse="war Vorgänger von",
    )[0]
    ging_hervor_aus.subj_class.clear()
    
    ging_hervor_aus.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ging_hervor_aus.obj_class.clear()
    
    ging_hervor_aus.obj_class.add(ContentType.objects.get(model=function.__name__))
    
    
    ist_untergeordnet = Property.objects.get_or_create(
        name="ist untergeordnet",
        name_reverse="hat untergeordnete Funktion",
    )[0]
    ist_untergeordnet.subj_class.clear()
    
    ist_untergeordnet.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ist_untergeordnet.obj_class.clear()
    
    ist_untergeordnet.obj_class.add(ContentType.objects.get(model=function.__name__))
    
    
    ausgeübt_in = Property.objects.get_or_create(
        name="ausgeübt in",
        name_reverse="war Ausübungsort von",
    )[0]
    ausgeübt_in.subj_class.clear()
    
    ausgeübt_in.subj_class.add(ContentType.objects.get(model=function.__name__))
    
    ausgeübt_in.obj_class.clear()
    
    ausgeübt_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    teil_von = Property.objects.get_or_create(
        name="Teil von",
        name_reverse="hat Teil",
    )[0]
    teil_von.subj_class.clear()
    
    teil_von.subj_class.add(ContentType.objects.get(model=place.__name__))
    
    teil_von.obj_class.clear()
    
    teil_von.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    zahlte_aus = Property.objects.get_or_create(
        name="zahlte aus",
        name_reverse="wurde ausbezahlt von",
    )[0]
    zahlte_aus.subj_class.clear()
    
    zahlte_aus.subj_class.add(ContentType.objects.get(model=institution.__name__))
    
    zahlte_aus.obj_class.clear()
    
    zahlte_aus.obj_class.add(ContentType.objects.get(model=salary.__name__))
    
    
    ist_gelegen_in = Property.objects.get_or_create(
        name="ist gelegen in",
        name_reverse="inkludiert",
    )[0]
    ist_gelegen_in.subj_class.clear()
    
    ist_gelegen_in.subj_class.add(ContentType.objects.get(model=institution.__name__))
    
    ist_gelegen_in.obj_class.clear()
    
    ist_gelegen_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    fand_statt_in = Property.objects.get_or_create(
        name="fand statt in",
        name_reverse="inkludierte",
    )[0]
    fand_statt_in.subj_class.clear()
    
    fand_statt_in.subj_class.add(ContentType.objects.get(model=event.__name__))
    
    fand_statt_in.obj_class.clear()
    
    fand_statt_in.obj_class.add(ContentType.objects.get(model=place.__name__))
    
    
    wurde_ausbezahlt_an = Property.objects.get_or_create(
        name="wurde ausbezahlt an",
        name_reverse="erhielt",
    )[0]
    wurde_ausbezahlt_an.subj_class.clear()
    
    wurde_ausbezahlt_an.subj_class.add(ContentType.objects.get(model=salary.__name__))
    
    wurde_ausbezahlt_an.obj_class.clear()
    
    wurde_ausbezahlt_an.obj_class.add(ContentType.objects.get(model=function.__name__))
    
    