from app.models import db, Movie_Image, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


def seed_movie_images():
    movie_image1 = Movie_Image(
        movie_id=1,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344401/The-Exorcist-_Believer_ef8gq1.jpg",
    )
    movie_image2 = Movie_Image(
        movie_id=2,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344379/Killers_of_the_Flower_Moon_wduley.jpg",
    )
    movie_image3 = Movie_Image(
        movie_id=3,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344400/The_Creator_nskkda.jpg",
    )
    movie_image4 = Movie_Image(
        movie_id=4,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344250/A_Haunting_in_Venice_vxf5lm.jpg",
    )
    movie_image5 = Movie_Image(
        movie_id=5,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344257/Dumb_Money_hbjylc.jpg",
    )
    movie_image6 = Movie_Image(
        movie_id=6,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344254/Blue-Beetle_x2i7qb.jpg",
    )
    movie_image7 = Movie_Image(
        movie_id=7,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344282/GranTurismo_viuvzv.jpg",
    )
    movie_image8 = Movie_Image(
        movie_id=8,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344354/HauntedMansion_iaxrgz.jpg",
    )
    movie_image9 = Movie_Image(
        movie_id=9,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344251/Barbie_fnnz3v.jpg",
    )
    movie_image10 = Movie_Image(
        movie_id=10,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344388/Oppenheimer_iqx708.jpg",
    )
    movie_image11 = Movie_Image(
        movie_id=11,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344413/Transformers-One_k0kwxu.jpg",
    )
    movie_image12 = Movie_Image(
        movie_id=12,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344252/beetlejuice-2-poster-1200x1500_kwui1c.jpg",
    )
    movie_image13 = Movie_Image(
        movie_id=13,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344252/beekeeper_ebq9sf.jpg",
    )
    movie_image14 = Movie_Image(
        movie_id=14,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344405/TheBookofClarence_o8scqh.jpg",
    )
    movie_image15 = Movie_Image(
        movie_id=15,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344260/FreudLastSession_a6ltib.jpg",
    )
    movie_image16 = Movie_Image(
        movie_id=16,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344250/Argylle_iasqtu.jpg",
    )
    movie_image17 = Movie_Image(
        movie_id=17,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344380/lisa_frankenstein_510x_elpgj3.webp",
    )
    movie_image18 = Movie_Image(
        movie_id=18,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344254/BobMarley-OneLove_vuyupu.jpg",
    )
    movie_image19 = Movie_Image(
        movie_id=19,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344379/KungFuPanda4_eooezk.jpg",
    )
    movie_image20 = Movie_Image(
        movie_id=20,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344263/ghostbusters-frozen-empire-one-sheet-i220258_zkufvx.jpg",
    )
    movie_image21 = Movie_Image(
        movie_id=21,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344263/GodzillaxKong-TheNewEmpire_oc6i4m.jpg",
    )
    movie_image22 = Movie_Image(
        movie_id=22,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344392/sonic-the-hedgehog-3-2024-poster-v0-vxcxhchro7gc1_rgrfpo.webp",
    )
    movie_image23 = Movie_Image(
        movie_id=23,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344392/Superbad_clfduw.jpg",
    )
    movie_image24 = Movie_Image(
        movie_id=24,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344406/TheHangover_jlzaya.jpg",
    )
    movie_image25 = Movie_Image(
        movie_id=25,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344254/Bridesmaids_xwjmqc.jpg",
    )
    movie_image26 = Movie_Image(
        movie_id=26,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344392/StepBrothers_bs5hog.jpg",
    )
    movie_image27 = Movie_Image(
        movie_id=27,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344353/GroundhogDay_o60kq7.jpg",
    )
    movie_image28 = Movie_Image(
        movie_id=28,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344383/MeanGirls_kauynh.jpg",
    )
    movie_image29 = Movie_Image(
        movie_id=29,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344258/DumbandDumber_ej8oyh.jpg",
    )
    movie_image30 = Movie_Image(
        movie_id=30,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344249/21JumpStreet_l3rqsp.jpg",
    )
    movie_image31 = Movie_Image(
        movie_id=31,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344402/The40-Year-OldVirgin_lke6d9.jpg",
    )
    movie_image32 = Movie_Image(
        movie_id=32,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344416/Zoolander_gttamn.jpg",
    )
    movie_image33 = Movie_Image(
        movie_id=33,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344354/Hereditary_nrsi5y.jpg",
    )
    movie_image34 = Movie_Image(
        movie_id=34,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344260/GetOut_vjr9xi.jpg",
    )
    movie_image35 = Movie_Image(
        movie_id=35,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344250/AQuietPlace_l2mz5w.jpg",
    )
    movie_image36 = Movie_Image(
        movie_id=36,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344405/TheConjuring_jnqjj3.jpg",
    )
    movie_image37 = Movie_Image(
        movie_id=37,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344376/ItFollows_qop9hg.jpg",
    )
    movie_image38 = Movie_Image(
        movie_id=38,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344384/Midsommar_fmf3xt.jpg",
    )
    movie_image39 = Movie_Image(
        movie_id=39,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344410/TheWitch_vqdgbs.jpg",
    )
    movie_image40 = Movie_Image(
        movie_id=40,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344413/Us_ejkqxu.jpg",
    )
    movie_image41 = Movie_Image(
        movie_id=41,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344391/Sinister_dldqz2.jpg",
    )
    movie_image42 = Movie_Image(
        movie_id=42,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344402/TheBabadook_ndkroe.jpg",
    )
    movie_image43 = Movie_Image(
        movie_id=43,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344409/TheNotebook_xfxjuz.jpg",
    )
    movie_image44 = Movie_Image(
        movie_id=44,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344388/PrideandPrejudice_nlpz3d.jpg",
    )
    movie_image45 = Movie_Image(
        movie_id=45,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344380/LaLaLand_i3qxri.jpg",
    )
    movie_image46 = Movie_Image(
        movie_id=46,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344251/AWalktoRemember_deovrd.jpg",
    )
    movie_image47 = Movie_Image(
        movie_id=47,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344410/Titanic_ojgynu.jpg",
    )
    movie_image48 = Movie_Image(
        movie_id=48,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344256/CrazyStupidLove_xvrjsj.jpg",
    )
    movie_image49 = Movie_Image(
        movie_id=49,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344406/TheFaultinOurStars_d3gspq.jpg",
    )
    movie_image50 = Movie_Image(
        movie_id=50,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344249/10ThingsIHateAboutYou_jvtzbb.jpg",
    )
    movie_image51 = Movie_Image(
        movie_id=51,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344388/NottingHill_nqbvfd.jpg",
    )
    movie_image52 = Movie_Image(
        movie_id=52,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344416/WhenHarryMetSally..._x0qgto.jpg",
    )
    movie_image53 = Movie_Image(
        movie_id=53,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344355/Inception_bdrlco.jpg"
    )
    movie_image54 = Movie_Image(
        movie_id=54,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344253/Blade_Runner_2049_tdtpi7.jpg"
    )
    movie_image55 = Movie_Image(
        movie_id=55,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344398/The_Matrix_o7zmco.jpg"
    )
    movie_image56 = Movie_Image(
        movie_id=56,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344376/Interstellar_scum5k.jpg"
    )
    movie_image57 = Movie_Image(
        movie_id=57,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344392/Star_Wars-_Episode_IV_-_A_New_Hope_srfwga.jpg"
    )
    movie_image58 = Movie_Image(
        movie_id=58,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344250/Arrival_cokidn.jpg"
    )
    movie_image59 = Movie_Image(
        movie_id=59,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344260/Ex_Machina_rhx4u7.jpg"
    )
    movie_image60 = Movie_Image(
        movie_id=60,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344397/The_Fifth_Element_gsexoi.jpg"
    )
    movie_image61 = Movie_Image(
        movie_id=61,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344259/Dune_snbfzm.jpg"
    )
    movie_image62 = Movie_Image(
        movie_id=62,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344260/Eternal_Sunshine_of_the_Spotless_Mind_emj194.jpg"
    )
    movie_image63 = Movie_Image(
        movie_id=63,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344383/Mad_Max-_Fury_Road_we0mhs.jpg"
    )
    movie_image64 = Movie_Image(
        movie_id=64,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344376/John_Wick_nnnqsx.jpg"
    )
    movie_image65 = Movie_Image(
        movie_id=65,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344257/Die_Hard_dmzaeu.jpg"
    )
    movie_image66 = Movie_Image(
        movie_id=66,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344397/The_Dark_Knight_bdoryl.jpg"
    )
    movie_image67 = Movie_Image(
        movie_id=67,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344263/Gladiator_jiu1mt.jpg"
    )
    movie_image68 = Movie_Image(
        movie_id=68,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344396/The_Avengers_kgr9ry.jpg"
    )
    movie_image69 = Movie_Image(
        movie_id=69,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344413/Transformers_hb3goh.jpg"
    )
    movie_image70 = Movie_Image(
        movie_id=70,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344255/Casino_Royale_ayanwn.jpg"
    )
    movie_image71 = Movie_Image(
        movie_id=71,
        img_url="https://res.cloudinary.com/dzsguqdmg/image/upload/v1728344385/Mission-_Impossible_-_Fallout_voxpij.webp"
    )

    movie_images = [
    movie_image1,
    movie_image2,
    movie_image3,
    movie_image4,
    movie_image5,
    movie_image6,
    movie_image7,
    movie_image8,
    movie_image9,
    movie_image10,
    movie_image11,
    movie_image12,
    movie_image13,
    movie_image14,
    movie_image15,
    movie_image16,
    movie_image17,
    movie_image18,
    movie_image19,
    movie_image20,
    movie_image21,
    movie_image22,
    movie_image23,
    movie_image24,
    movie_image25,
    movie_image26,
    movie_image27,
    movie_image28,
    movie_image29,
    movie_image30,
    movie_image31,
    movie_image32,
    movie_image33,
    movie_image34,
    movie_image35,
    movie_image36,
    movie_image37,
    movie_image38,
    movie_image39,
    movie_image40,
    movie_image41,
    movie_image42,
    movie_image43,
    movie_image44,
    movie_image45,
    movie_image46,
    movie_image47,
    movie_image48,
    movie_image49,
    movie_image50,
    movie_image51,
    movie_image52,
    movie_image53,
    movie_image54,
    movie_image55,
    movie_image56,
    movie_image57,
    movie_image58,
    movie_image59,
    movie_image60,
    movie_image61,
    movie_image62,
    movie_image63,
    movie_image64,
    movie_image65,
    movie_image66,
    movie_image67,
    movie_image68,
    movie_image69,
    movie_image70,
    movie_image71
    ]


    for image in movie_images:
        db.session.add(image)
    db.session.commit()

def undo_movie_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.movie_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM movie_images"))

    db.session.commit()
