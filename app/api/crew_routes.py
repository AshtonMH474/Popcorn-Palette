from flask import Blueprint, jsonify,request
from flask_login import login_required
from app.models import Artist,db
from app.models.artist import crew

crew_routes = Blueprint('crew',__name__)

@crew_routes.route('/<int:movie_id>')
def get_crew(movie_id):

    # grabs all the artist with from crew with this movie Id
    artists = db.session.query(Artist).join(crew,Artist.id == crew.c.artist_id).filter_by(movie_id = movie_id).all()

    artist_list =[]
    for artist in artists:
        # turns every artist in json format
        crew_entry = db.session.query(crew).filter_by(movie_id=movie_id, artist_id=artist.id).first()
        artist_list.append({
            'id': artist.id,
            'firstName': artist.first_name,
            'lastName':artist.last_name,
            'imgUrl':artist.img_url,
            'role': crew_entry.role,
            'played': crew_entry.played
        })

    return jsonify(artist_list)
