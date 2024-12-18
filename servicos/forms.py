from django.forms import ModelForm
from .models import Servico, CategoriaManuntencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields['título'].widget.attrs.update({'placeholder':field})

        choices = list()
        for i, j in self.fields['categoria_manuntencao'].choices:
            categoria = CategoriaManuntencao.objects.get(título=j)
            choices.append((i.value, categoria.get_título_display()))
      
        self.fields['categoria_manuntecao'].choices = choices