from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker, scoped_session
from operacje import create_engine_sqlalchemy, Ksiazka, Base

app = Flask(__name__)

engine = create_engine_sqlalchemy()
Base.metadata.create_all(engine)
SessionLocal = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def home():
  return "<h1>Przyjacielskie wypozyczenia ksiazek</h1>"

@app.route('/ksiazki', methods=['GET'])
def get_all_ksiazki():
  with SessionLocal() as session:
    ksiazki = session.query(Ksiazka).all()
    ksiazki_list = [{
      "id": ksiazka.id,
      "autor": ksiazka.autor,
      "tytul": ksiazka.tytul,
      "rok_wydania": ksiazka.rok_wydania
    } for ksiazka in ksiazki]
    return jsonify(ksiazki_list)
  
@app.route('/ksiazka/<int:id>', methods=['GET'])
def get_ksiazka(id):
  with SessionLocal() as session:
    ksiazka = session.query(Ksiazka).filter_by(id=id).first()
    if ksiazka:
      return jsonify({
        "id": ksiazka.id,
        "autor": ksiazka.autor,
        "tytul": ksiazka.tytul,
        "rok_wydania": ksiazka.rok_wydania
      })
    else:
      return jsonify({"message": "Ksiazka nie istnieje."}), 404
       
@app.route('/ksiazka/<int:id>', methods=['DELETE'])
def delete_ksiazka(id):
  with SessionLocal() as session:
    ksiazka = session.query(Ksiazka).get(id)
    if ksiazka:
      session.delete(ksiazka)
      session.commit()
      print(f"Usunieto ksiazke: {ksiazka}")
      return jsonify({'status': 'OK'})
    else:
      return jsonify({"message": "Ksiazka nie istnieje."}), 404

@app.route('/ksiazka/<string:autor>/<string:tytul>/<int:rok_wydania>', methods=['POST'])
def dodaj_ksiazke(autor, tytul, rok_wydania):
  with SessionLocal() as session:
    ksiazka = Ksiazka(autor=autor, tytul=tytul, rok_wydania=rok_wydania)
    session.add(ksiazka)
    session.commit()
    print(f"Dodano ksiazke: {ksiazka}")
    return jsonify({'status': 'OK'})
  
@app.route('/ksiazka/<int:id>', methods=['PUT'])
def update_ksiazka(id):
  with SessionLocal() as session:
    ksiazka = session.query(Ksiazka).get(id)
    if ksiazka:
      ksiazka.autor = request.json['autor']
      ksiazka.tytul = request.json['tytul']
      ksiazka.rok_wydania = request.json['rok_wydania']
      session.commit()
      print(f"Zaktualizowano ksiazke: {ksiazka}")
      return jsonify({'status': 'OK'})
    else:
      return jsonify({"message": "Ksiazka nie istnieje."}), 404

if __name__ == "__main__":
  app.run()