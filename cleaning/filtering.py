import os
import json

# [
#   {
#     "answer": {
#       "is_flower": true,
#       "is_flower_confidence": "high",
#       "is_single_type_of_flower": true,
#       "is_single_type_of_flower_confidence": "high",
#       "common_name": "Rose",
#       "scientific_name": "Rosa"
#     },
#     "metadata": {
#       "DescriptionRose Garden (50132012516).jpg": "Royal Botanical Gardens. Burlington/Hamilton, ON",
#       "Date": "2 July 2018, 00:00",
#       "Source": "Rose Garden",
#       "Author": "Vladislav Litvinov"
#     },
#     "uuid": "2fbd83b2-e1d4-444b-8594-8caa320f2620",
#     "model": "claude-3-haiku-20240307"
#   },

_input_file = os.environ.get(
    "METADATA_ONLY_RESPONSES_FILE",
    "data/processed/claude_metadata_only_responses.json",
)
_output_file = os.environ.get(
    "SINGLE_FLOWERS_ONLY_FILE",
    "data/processed/single_flowers_only_responses.json",
)


def main():
    # load claude metadata only responses
    with open(_input_file, "r") as f:
        responses = json.load(f)

    # filter out responses that are is_flower
    flowers_only = filter(lambda x: x["answer"]["is_flower"], responses)

    # filter out responses that are is_single_type_of_flower
    single_flowers_only = filter(
        lambda x: x["answer"]["is_single_type_of_flower"], flowers_only
    )

    single_flowers_only = list(single_flowers_only)

    # save single flowers only responses
    with open(_output_file, "w") as f:
        json.dump(single_flowers_only, f, indent=2)

    all_flower_names = set()
    for response in single_flowers_only:
        all_flower_names.add(response["answer"]["common_name"])

    all_scientific_names = set()
    for response in single_flowers_only:
        all_scientific_names.add(response["answer"]["scientific_name"])

    # save all flower names
    with open("data/processed/all_flower_names.json", "w") as f:
        json.dump(list(all_flower_names), f, indent=2)

    already_clustered = set()
    for cluster_name, cluster in _clusters_1.items():
        already_clustered.update(cluster)

    unclustered = all_scientific_names - already_clustered

    # save all scientific names
    with open("data/processed/all_scientific_names_1.json", "w") as f:
        json.dump(list(unclustered), f, indent=2)


_clusters = {
    "Rosa (Garden Roses)": [
        "Rosa 'My Hero'",
        "Rosa 'Crocus Rose' David Austin",
        "rosa 'murray'",
        "Rosa 'WEKblufytirar'",
        "Rosa centifolia 'Pomponia'",
        "Rosa 'Golden Monica'",
        "Rosa 'Harmony'",
        "Rosa 'White Cockade'",
        "Rosa ×hybrida",
        "Rosa 'Van Fleet'",
        "Rosa x hybrida",
        "Rosa 'Colette'",
        "Rosa La Touche",
        "Rosa Santana",
        "Rosa 'Jan Spek'",
        "Rosa 'Sunsprite'",
        "Rosa 'California Dreaming'",
        "Rosa 'Fukuyama-Rose'",
        "Rosa 'Flamingo'",
        "Rosa 'Red Lion'",
        "Rosa Indica",
        "Rosa 'Aspirin Rose'",
        "Rosa 'Sophy's Rose'",
        "Rosa 'Maréchal Niel'",
        "Rosa 'Constance Spry'",
        "Rosa 'Rainbow'",
        "Rosa 'Adélaïde d'Orléans'",
        "Rosa 'Bernstein-Rose'",
        "Rosa 'Saturday'",
        "Rosa 'Garden Rose'",
        "Rosa amarilla",
        "Rosa 'Top Gun'",
        "Rosa 'La Rose de Molinard'",
        "Rosa x anglica",
        "Rosa 'Cromarty'",
        "Rosa 'Sweet Delight'",
        "Rosa 'Pomponella'",
        "Rosa hurdalsrosa",
        "Rosa quarzosa",
        "Rosa 'Strombergzauber'",
        "Rosa 'WW II Memorial Rose'",
        "Rosa 'Eden Rose'",
        "Rosa 'Novalis'",
        "Rosa × isparta",
        "Rosa 'Carefree Wonder'",
        "Rosa 'Bordure Rose No. 2'",
        "Rosa 'Princess Margaret Rose'",
        "Rosa 'Sedana'",
        "Rosa hybrid",
        "Rosa 'Rose des 4 vents'",
        "Rosa 'Téquila'",
        "Rosa 'Lions Rose'",
        "Rosa 'Red'",
        "Rosa 'Ingrid Weibull'",
        "Rosa 'Annapurna'",
        "Rosa 'Souvenir de Brod'",
        "Rosa cromartiensis",
        "Rosa hybrida 'American Beauty'",
        "Rosa 'Felicitas'",
        "Rosa 'Winter Sun'",
        "Rosa pendulina",
        "Rosa 'Bernstein Rose'",
        "Rosa 'Regierungsrat Rottenberger'",
        "Rosa 'Veilchenblau'",
        "Rosa 'Gebrüder Grimm'",
        "Rosa 'Rose Rhapsody'",
        "Rosa 'Wedding Piano'",
        "Rosa 'Kurstadt Baden'",
        "Rosa 'Robin Hood' Pemberton 1927",
        "Rosa hemisphaerica",
        "Rosa 'Bordure Rose'",
        "Rosa bengalensis",
        "Rosa 'Rose de Molinard'",
        "Rosa 'Christchurch'",
        "Rosa 'Johann Strauss'",
        "Rosa sp. cv.",
        "Rosa 'Albert-Georg-Pluta-Rose'",
        "Rosa 'Pink Border Rose'",
        "Rosa 'Pink Parfait'",
        "Rosa x 'Blue'",
        "Rosa 'Pink Eden Rose'",
        "Rosa 'Oh Happy Day'",
        "Rosa 'Cherry Lips'",
        "Rosa 'Kaiserin Elisabeth'",
        "Rosa 'Biscuit rose de Reims'",
        "Rosa 'Zambra'",
        "Rosa 'Rose du Roi'",
        "Rosa 'White Fleurette'",
        "Rosa 'Faanya'",
        "Rosa X harisonii",
        "Rosa augusta luise",
        "Rosa lutea",
        "Rosa 'Sunset Celebration'",
        "Rosa 'Eureka'",
        "Rosa Canina",
        'Rosa "Apricot"',
        "Rosa Rubra",
        "Rosa 'Raymond Nazereau'",
        "Rosa 'Cigarette'",
        "Rosa 'Rock & Roll'",
        "Rosa 'Parole'",
        "Rosa 'Pride of England'",
        "Rosa tomentosa",
        "Rosa 'Gold Medal'",
        "Rosa 'Garden'",
        "Rosa 'Snow Carpet'",
        "Rosa 'Hermann Schmidt'",
        "Rosa 'Naheglut'",
        "Rosa 'Aquarius'",
        "Rosa 'Radrazz'",
        "Rosa banksiae Lutea",
        "Rosa 'The Squire'",
        "Rosa 'Border Rose'",
        "Rosa 'Starlet Rose Eva'",
        "Rosa 'Mona Lisa'",
        "Rosa 'Olympia'",
        "Rosa 'Violetta'",
        "Rosa 'Chapeau de Napoleon'",
        "Rosa 'Golden Rose'",
        "Rosa 'Knock Out'",
        "Rosa lilacina",
        "Rosa 'Stadt Kiel'",
        "Rosa 'Marechal Niel'",
        "Rosa cv.",
        "Rosa 'Apricot'",
        "Rosa peldonii",
        "Rosa Golden Border",
        "Rosa Pat Austin",
        "Rosa 'Strawberry Ice'",
        "Rosa 'Gerbe Rose'",
        "Rosa 'Unicef-Rose'",
        "Rosa 'Pink'",
        "Rosa 'Rose de Resht'",
        "Rosa x cultivar",
        "Rosa parviflora",
        "Rosa x hybrida 'Yellow'",
        "Rosa 'Discovery'",
        "Rosa saintroseana",
        "Rosa 'Lady Mary Fitzwilliam'",
        "Rosa 'Frau Astrid Späth'",
        "Rosa 'New Dawn'",
        "Rosa 'Red Finesse'",
        "Rosa sweginzowii 'macrocarpa'",
        "Rosa 'Saga'",
        "Rosa 'Robe Rose'",
        "Rosa 'Heyden'",
        "Rosa × floribunda",
        "Rosa 'Pink Spray'",
        "Rosa 'Double Delight'",
        "Rosa spec.",
        "Rosa rubiginosa",
        "Rosa 'Yellow Romantica'",
        "rosa aspirin rose",
        "Rosa 'Yvonne Rabier'",
        "Rosa species",
        "Rosa 'Vicky 93'",
        "Rosa laevingata",
        "Rosa 'Rose Cascade'",
        "Rosa hibernica",
        "Rosa 'Gypsy Soul'",
        "Rosa 'Elmshorn'",
        "Rosa muscosa",
        "Rosa 'Marie Curie'",
        "Rosa 'Sahara'",
        "Rosa 'The McCartney Rose'",
        "Rosa centifolia var. muscosa",
        "Rosa 'Ballade'",
        "Rosa 'Peace Memorial'",
        "Rosa 'Kronjuwel'",
        "Rosa canina",
        "Rosa 'Charisma'",
        "Rosa x 'Baccara'",
        "Rosa L.",
        "Rosa 'LandFrauen Rose'",
        "Rosa 'Confidence'",
        "Rosa 'Summer Lady'",
        "Rosa 'Cottage Rose'",
        "Rosa 'Königin der Rosen'",
        "Rosa species (likely Rosa x hybrid)",
        "Rosa 'Pope John Paul II'",
        "Rosa 'Rose-Marie Viaud'",
        "Rosa x Xanthina",
        "Rosa × aurea",
        "Rosa cinnamomea",
        "Rosa 'Lady Emma Hamilton'",
        "Rosa Heidekönigin",
        "Rosa 'Pretty Jessica'",
        "Rosa 'APPLAUSE'",
        "Rosa 'Sodenia'",
        "Rosa waimarie",
        "Rosa 'Princess Adelaide'",
        "Rosa × hybrida",
        "Rosa 'Ruby Rose'",
        "Rosa 'Maxi Vita'",
        "Rosa centifolia muscosa",
        "Rosa chinensis",
        "Rosa montana",
        "Rosa 'Ange'",
        "Rosa florett",
        "Rosa 'Apache'",
        "Rosa 'Westzeit'",
        "Rosa 'Peace'",
        "Rosa 'Périgord Blanc'",
        "Rosa 'MEIzolle'",
        "Rosa 'Eglantyne'",
        "Rosa 'Frau Sophie Meyerholz'",
        "Rosa 'Masquerade'",
        "Rosa 'The Ancient Mariner'",
        "Rosa 'Nina Weibull'",
        "Rosa 'Sparrieshoop'",
        "Rosa floribunda 'WEKblufytirar'",
        'Rosa "Blue rose"',
        "Rosa 'Cherry Parfait'",
        "Rosa Tantau's Bernsteinrose",
        "Rosa 'Black-Forrest-Rose'",
        "Rosa 'Sourire d'Orchidée'",
        "Rosa 'Morning Sun'",
        "Rosa damascena",
        "Rosa 'Apricot Nectar'",
        "Rosa 'Kinrenpo'",
        "Rosa 'Golden Showers'",
        "Rosa gallica",
        "Rosa 'Margaret Merril'",
        "Rosa setipoda",
        "Rosa 'Martin des Senteurs'",
        "Rosa 'Mme Norbert Levavasseur'",
        "Rosa 'Comte Frédéric de Thun-Hohenstein'",
        "Rosa compassa",
        "Rosa 'Jules Margottin'",
        "Rosa centifolia",
        "Rosa 'Yorkshire'",
        "Rosa 'Sourire Rose'",
        "Rosa 'Sommerabend'",
        "Rosa alpina",
        "Rosa 'Lady Norwood'",
        "Rosa 'Graham Thomas'",
        "Rosa 'Kristall'",
        "Rosa 'Five Colored Rose'",
        "Rosa 'Hurdalsrosa'",
        "Rosa 'Crocus Rose'",
        "Rosa 'Princesse de Nassau'",
        "Rosa x ananassa",
        "Rosa dumalis",
        "Rosa 'Heart of Gold'",
        "Rosa 'Black Magic'",
        "Rosa 'Else Poulsen'",
        "Rosa 'Centro-Rose'",
        "Rosa 'Operettenrose'",
        "Rosa 'Dublin Bay'",
        'Rosa "Discovery 2009"',
        "Rosa 'Lions-Rose'",
        "rosa alba",
        "Rosa 'Mary Rose'",
        "Rosa 'Madame Pierre Oger'",
        "Rosa 'Kaguyahime'",
        "Rosa × damascena",
        "Rosa 'Inspiration'",
        "Rosa xanthina",
        "Rosa 'Hatsukoi'",
        "Rosa 'Biscuit Rose de Reims'",
        "Rosa 'Aprilia Red'",
        "Rosa 'Papagena'",
        "Rosa Apricot Nectar",
        "Rosa 'Helmut Kohl'",
        "Rosa 'Amanogawa'",
        "Rosa Léo Ferré",
        "Rosa parma",
        "Rosa 'England's Rose'",
        "Rosa 'Lady of Shalott'",
        "Rosa 'Schneewittchen'",
        "Rosa 'Guirlande Rose'",
        "Rosa chinensis var. viridiflora",
        "Rosa pimpinellafolia",
        "Rosa 'Isarperle'",
        "Rosa 'Abraham Darby'",
        "Rosa 'Candy Rose'",
        "Rosa agrestis",
        "Rosa alba",
        "Rosa 'Blue Bijou'",
        "Rosa 'Meissen'",
        "Rosa sp.",
        "Rosa 'Sympathie'",
        "Rosa 'The Alnwick Rose'",
        "Rosa 'Kommerzienrat W. Rautenstrauch'",
        "Rosa 'Quatre Saisons Blanc Mousseux'",
        "Rosa 'Black Boy'",
        "Rosa floydii",
        "Rosa 'Aloha'",
        "Rosa 'Queen Elisabeth'",
        "Rosa 'Marguerite Rose'",
        "Rosa 'Paper Doll'",
        "Rosa 'Perlinoë'",
        "Rosa 'Orange'",
        "Rosa 'Madame Falcot'",
        "Rosa 'IGA Erfurt'",
        "Rosa 'Bridal Pink'",
        "Rosa 'Aspirin-Rose'",
        "Rosa multiflora",
        "Rosa 'Botticelli'",
        "Rosa 'Aimée Vibert'",
        "Rosa x",
        "Rosa 'Rose de Tolbiac'",
        "Rosa 'Paul Transon'",
        "Rosa 'Ambridge Rose'",
        "Rosa hybrida",
        "Rosa 'Heidi Klum'",
        "Rosa 'Perle des jardins'",
        "Rosa 'Black-Forest-Rose'",
        "Rosa 'Hella'",
        "Rosa indica",
        "Rosa 'Grandiflora'",
        "Rosa 'Joe Polowsky Friedensrose'",
        "Rosa 'Rose Vézelay'",
        "Rosa 'Petticoat'",
        "Rosa 'Lady Rose'",
        "Rosa 'Rose de Rescht'",
        "Rosa 'Versicolor'",
        "Rosa 'Moon Shadow'",
        "Rosa 'Kansha'",
        "Rosa 'Salmon Sunblaze'",
        "Rosa 'Diamant Rose'",
        "Rosa Aspirin Rose",
        "Rosa 'Black Forest Rose'",
        "Rosa 'Rose Dot'",
        "Rosa 'President Hoover'",
        "Rosa 'Auguste Renoir'",
        "Rosa 'Blush Noisette'",
        "Rosa 'Lolita'",
        "Rosa 'Yellow'",
        "Rosa Xanthina",
        "Rosa 'Robin Hood'",
        "Rosa 'Blue Eyes'",
        "Rosa mandarine symphonie",
        "Rosa 'Rote Czárdás'",
        "Rosa 'Miss Baden'",
        "Rosa 'Gold'",
        "Rosa 'brimstone'",
        "Rosa 'Uetersen'",
        "Rosa x hybrid",
        "rosa 'ange rose'",
        "Rosa floribunda",
        "Rosa 'Tchaikowski'",
        "Rosa 'Rosamunde'",
        "Rosa 'Chrysler Imperial'",
        "Rosa 'Tahitian Sunset'",
        "Rosa 'Ida Klemm'",
        "Rosa 'Michelangelo'",
        "Rosa (genus)",
        "Rosa 'Dunwich Rose'",
        "Rosa 'Tropicana'",
        "Rosa virginiana",
        "Rosa carolina",
        "Rosa × alba",
        "Rosa rubra",
        "Rosa mutabilis",
        "Rosa Alba Maxima",
        "Rosa 'Madame de Montespan'",
        "Rosa 'Chrysler'",
        "Rosa 'Spanish Beauty'",
        "Rosa 'Schwarze Madonna'",
        "Rosa lacerata",
        "Rosa 'Thalia'",
        "Rosa 'Louise-Catherine Breslau'",
        "Rosa 'LLX 9059'",
        "Rosa 'Rose of Tralee'",
        "Rosa 'Anne de Bretagne'",
        "Rosa 'Tudor'",
        "Rosa moschata",
        "Rosa 'Rotilia'",
        "Rosa 'Helmut Kohl Rose'",
        "Rosa 'White Dorothy'",
        "Rosa Milkmaid",
        "Rosa pimpinellifolia",
        "Rosa 'Blue Bird'",
        "Rosa spithamea",
        "Rosa Blue Bajou",
        "Rosa 'Prairie Snowdrift'",
        "Rosa 'Fragola'",
        "Rosa 'Kiftsgate'",
        "Rosa 'Alba'",
        "Rosa 'Maman Cochet'",
        "Rosa 'Angela'",
        "Rosa Eden",
        "Rosa rugosa",
        "Rosa 'Sekel'",
        "Rosa 'Variegata di Bologna'",
        "Rosa 'Moonsprite'",
        "Rosa 'Julie'",
        "Rosa 'Cathedral'",
        "Rosa 'La Rose Optimiste'",
        "Rosa 'Blue'",
        "Rosa 'Perfume Delight'",
        "Rosa cornetti",
        "Rosa 'Bernd-Weigel-Rose'",
        "Rosa Black Pearl",
        "Rosa autumnalis",
        "Rosa 'Martha Washington'",
        "Rosa 'Sunshine Daydream'",
        "Rosa centifolia 'Muscosa'",
        "Rosa 'Heidi Klum-Rose'",
        "Rosa 'Westpoint'",
        "Rosa x damascena 'Nigra'",
        "Rosa 'Karl Ploberger'",
        "Rosa 'Cornetto'",
        "Rosa 'Konrad Adenauer'",
        "Rosa japonica",
        "Rosa 'Chaucer'",
        "Rosa Inka Floribunda",
        "Rosa 'Pink Grootendorst'",
        "Rosa 'Marie-Antoinette'",
        "Rosa 'Kuro-Shinjyu'",
        "Rosa 'Trompeter von Säckingen'",
        "Rosa 'Rock and Roll'",
        "Rosa 'Gold of Ophir'",
        "rosa",
        "Rosa x hytbrida",
        "Rosa 'Sainte Rose'",
        "Rosa 'Griseldis'",
        "Rosa woodsii",
        "Rosa 'Kammersänger Karl Terkal'",
        "Rosa 'Iceberg'",
        "Rosa x cornetto",
        "Rosa 'Innocencia'",
        "Rosa 'Rose Gaujard'",
        "Rosa heatherae",
        "Rosa 'Voyage'",
        "Rosa x harisonii",
        "Rosa spp.",
        "Rosa",
        "Rosa 'Antoine Rivoire'",
        "Rosa 'English Mist'",
        "Rosa 'American Beauty'",
        "Rosa 'Blue Moon'",
        "Rosa x alba",
        "Rosa 'Trigintipetala'",
        "Rosa 'Avalanche'",
        "Sainte Rose",
        "Rosa 'Sugandha'",
    ],
    "Viola": [
        "Viola x wittrockiana 'Dynamite Rose with Blotch'",
        "Viola x wittrockiana 'Delta Pure Rose'",
        "Viola x wittrockiana 'Matrix Rose Blotch'",
        "Viola 'Panola Rose Picotee'",
        "Viola x wittrockiana",
        "Viola x wittrockiana 'Colossus Rose Blotch'",
        "Viola",
    ],
    "Fuchsia": [
        "Fuchsia sp.",
        "Fuchsia",
        "Fuchsia speciosa 'Rose of Castile Improved'",
        "Fuchsia hybrid",
        "Fuchsia 'Rose of Castile Improved'",
        "Fuchsia 'Rose of Denmark'",
        "Fuchsia 'Rose Phenominal'",
        "Fuchsia 'Rose Phenomenal'",
    ],
    "Dahlia": ["Dahlia spp.", "Dahlia", "Dahlia sp."],
    "Iris": ["Iris spp.", "Iris", "Iris 'Secondhand Rose'"],
    "Begonia": [
        "Begonia sp.",
        "Begonia 'Ambassador Rose'",
        "Begonia 'Green Leaf Rose'",
    ],
    "Narcissus": ["Narcissus", "Narcissus 'Rose Caprice'"],
    "Nymphaea": ["Nymphaea", "Nymphaeaceae"],
    "Tulipa": [
        "Tulipa sp.",
        "Tulipa",
        "Tulipa spp.",
        "Tulipa 'Duc van Tol Rose'",
        "Tulipa genus",
    ],
    "Camellia": ["Camellia japonica"],
    "Pentas": ["Pentas lanceolata", "Pentas lanceolata 'Lava Rose'"],
    "Hemerocallis": ["Hemerocallis fulva", "Hemerocallis 'Neyron Rose'"],
    "Canna": [
        "Canna × generalis 'Cannova Rose'",
        "Canna × generalis",
        "Canna x generalis",
    ],
    "Calibrachoa": ["Calibrachoa hybrida 'Cabaret Cherry Rose'"],
    "Rhododendron": [
        "Rhododendron 'Anna Rose Whitney'",
        "Rhododendron x Girard 'Girard's Rose'",
        "Rhododendron 'Choptank Rose'",
        "Rhododendron",
        "Rhododendron ponticum",
    ],
    "Dianthus": [
        "Dianthus deltoides",
        "Dianthus 'Telstar Carmine Rose'",
        "Dianthus deltoides 'Zing Rose'",
        "Dianthus caryophyllus",
    ],
    "Pelargonium": ["Pelargonium", "Pelargonium graveolens"],
    "Primula": ["Primula vulgaris 'April Rose'", "Primula vulgaris"],
    "Petunia": ["Petunia 'Wave Rose'", "Petunia 'Ultra Rose'"],
    "Hydrangea": ["Hydrangea macrophylla"],
    "Impatiens": [
        "Impatiens walleriana 'Fiesta Ole Rose'",
        "Impatiens × hybrida",
        "Impatiens 'Super Elfin Rose'",
    ],
    "Zinnia": ["Zinnia elegans 'Uproar Rose'", "Zinnia elegans"],
    "Cheiranthus": ["Cheiranthus 'Charity Rose Red'"],
    "Echinacea": ["Echinacea purpurea"],
    "Hibiscus": [
        "Hibiscus syriacus",
        "Hibiscus moscheutos",
        "Hibiscus rosa-sinensis",
        "Hibiscus",
    ],
    "Salvia": [
        "Salvia nemorosa",
        "Salvia nemorosa 'Rose Queen'",
        "Salvia nemorosa 'Sensation Rose'",
    ],
    "Achillea": ["Achillea millefolium 'Oertel's Rose'"],
    "Paeonia": ["Paeonia"],
    "Helianthus": ["Helianthus", "Helianthus annuus"],
    "Calluna": ["Calluna vulgaris"],
    "Leucanthemum": ["Leucanthemum vulgare"],
    "Magnolia": ["Magnolia stellata", "Magnolia x soulangeana"],
    "Lilium": ["Lilium"],
    "Adenium": ["adenium obesum", "Adenium obesum", "Adenium"],
    "Bellis": ["Bellis perennis"],
    "Lavandula": ["Lavandula", "Lavandula spp."],
    "Hypericum": ["Hypericum perforatum"],
    "Chrysanthemum": ["Chrysanthemum"],
    "Berberis": [
        "Berberis thunbergii",
        "Berberis thunbergii f. atropurpurea",
        "Berberis thunbergii var. Atropurpurea 'Rose Glow'",
    ],
    "Veronica": ["Veronica officinalis"],
    "Arachis": ["Arachis pintoi"],
    "Cleome": ["Cleome hassleriana 'Sparkler Rose'", "Cleome hassleriana"],
    "Pachliopta": [
        "Pachliopta aristolochiae aristolochiae",
        "Pachliopta aristolochiae",
    ],
    "Tolpis": ["Tolpis barbata"],
    "Phoenicopterus": ["Phoenicopterus roseus"],
    "Taraxacum": ["Taraxacum officinale", "Taraxacum"],
    "Nerium": ["Nerium oleander"],
    "Armeria": ["Armeria maritima"],
    "Arge": ["Arge pagana stephensii"],
    "Pieris": ["Pieris japonica"],
    "Curcuma": ["Curcuma zedoaria"],
    "Alyssum": ["Alyssum 'Easter Bonnet Deep Rose'"],
    "Iresine": ["Iresine Blazin Rose"],
    "Convolvulus": ["Convolvulus arvensis"],
    "Orchis": ["Orchis mascula"],
    "Nelumbo": ["Nelumbo nucifera"],
    "Cistus": ["Cistus"],
    "Misumena": ["Misumena vatia"],
    "Allium": [
        "Allium ampeloprasum var. holzmannii",
        "Allium sativum 'Pink'",
        "Allium roseum",
    ],
    "Tagetes": ["Tagetes sp.", "Tagetes sp. cv."],
    "Aubrieta": ["Aubrieta"],
    "Bougainvillea": ["Bougainvillea"],
    "Freesia": ["Freesia", "Freesia spp."],
    "Epimedium": ["Epimedium grandiflorum"],
    "Prunus": ["Prunus serrulata"],
    "Trifolium": ["Trifolium repens"],
    "Viburnum": ["Viburnum opulus"],
    "Cymbidium": ["Cymbidium x cultivar"],
    "Macroptilium": ["Macroptilium lathyroides"],
    "Kolkwitzia": ["Kolkwitzia amabilis"],
    "Delosperma": ["Delosperma cooperi"],
    "Diplolepis": ["Diplolepis ignota"],
    "Tecomaria": ["Tecomaria capensis 'Hammer's Rose'"],
    "Zingiber": ["Zingiber officinale"],
    "Jacaranda": ["Jacaranda", "Jacanda"],
    "Maniola": ["Maniola jurtina"],
    "Vaccinium": ["Vaccinium vitis-idaea"],
    "Holcoglossum": ["Holcoglossum tsii"],
    "Agapanthus": ["Agapanthus"],
    "Dendrobium": ["Dendrobium bigibbum"],
    "Unknown": [
        "Raadts wisselward",
        "unknown",
        "Unknown",
        "Quartz (variety rose)",
        "Florem Sancti Dionysii",
        "Flowers",
        "Fleur",
        "Angiosperm",
        "Flower",
        "not enough information to determine",
        "Unspecified",
        "Plantae",
        "Brésil quartz rose",
        "Grand ílet",
        "Rosa quartz",
        "Flora",
        "None",
        "Hortus florens",
        "unspecified",
        "selenite",
        "Magnoliophyta",
        "Philatelica",
        "Mariae",
        "Marian flora",
        "Asteraceae",
        "Phalanger",
        "Quartz",
        "Quartz rose",
        "Flos spp.",
        "Quartz var. rose quartz",
        "N/A",
        "Plessis-Nogent macaque",
        "Flos",
    ],
}

_clusters_to_avoid = {
    "Rosa (Garden Roses)",
    "unlabelled",
    "Unknown",
}


def main_1():
    # load flowers only
    with open(_output_file, "r") as f:
        flowers_only = json.load(f)

    # make a "specific_flower": "cluster" dict
    specific_flower_cluster = {}
    for cluster_name, cluster in _clusters.items():
        for flower in cluster:
            specific_flower_cluster[flower] = cluster_name

    # cluster flowers
    clustered_flowers = {}
    for response in flowers_only:
        flower = response["answer"]["scientific_name"]
        if flower in specific_flower_cluster:
            cluster = specific_flower_cluster[flower]
        else:
            cluster = "unlabelled"

        if cluster not in clustered_flowers:
            clustered_flowers[cluster] = []

        clustered_flowers[cluster].append(response)

    # get cluster counts
    cluster_counts = {}
    for cluster, flowers in clustered_flowers.items():
        cluster_counts[cluster] = len(flowers)

    output_file = "data/processed/clustered_flowers.json"
    with open(output_file, "w") as f:
        json.dump(
            {"clustered_flowers": clustered_flowers, "cluster_counts": cluster_counts},
            f,
            indent=2,
        )

    all_flowers_from_good_clustes = []
    for cluster, flowers in clustered_flowers.items():
        if cluster in _clusters_to_avoid:
            continue

        # add cluster to the flower objects
        for flower in flowers:
            flower["cluster"] = cluster

        all_flowers_from_good_clustes.extend(flowers)

    output_file = "data/processed/all_flowers_from_good_clusters.json"
    with open(output_file, "w") as f:
        json.dump(all_flowers_from_good_clustes, f, indent=2)

    good_flower_uuids = [flower["uuid"] for flower in all_flowers_from_good_clustes]
    with open("data/processed/good_flower_uuids.json", "w") as f:
        json.dump(good_flower_uuids, f, indent=2)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    # main()
    main_1()
