class Stamp(FlaskForm):
    gebiet = StringField('Gebiet', validators=[DataRequired()])
    jahrgang = IntegerField('Jahrgang')
    satz = StringField('Satz')
    michnr = IntegerField('MichNr')
    entwertung = StringField('Entwertung', validators=[DataRequired()])
    anzahl = IntegerField('Anzahl')
    bild = StringField('Bild')
