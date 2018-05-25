# -*- coding: utf-8 -*-
#
# Instalacion de paquetes -->
# 1. Instalar sphinx latex
# 2. Instalar numfig del siguiente link --> https://sourceforge.net/p/numfig/wiki/Home/  
# Y ejecutar --> python -c 'import sphinx' .
# Descomprimir, y ejecutar python setup.py install


#
# INSTRUCCIONES PARA COMPILAR -->
# 1. Ejecutar el siguiente comando para compilar
# $ make latexpdf
# 2. El documento final se encuentra en _build/ con el nombre prueba.pdf.
#
# prueba documentation build configuration file, created by
# sphinx-quickstart on Sat Apr 29 16:57:03 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'tesis'
copyright = u'2017, Rodrigo'
author = u'Rodrigo'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pruebadoc'


# -- Options for LaTeX output ---------------------------------------------
import os
path = os.getcwd().replace('/','//')


latex_additional_files = []

#Clase base de sphinx manual -->

#https://github.com/basespace/basespace-python-sdk/blob/master/doc/latex/sphinxmanual.cls
#/usr/local/lib/python2.7/dist-packages/sphinx/texinputs/sphinxmanual.cls


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
     'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
     'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',
    #'preamble': ''' 
    #                \\begin{organizacion}
    #                First document. This is a simple example, with no 
    #                extra parameters or packages included.
    #                \\end{organizacion} 
    #                ''',
    'atendofbody': '''First document. This is a simple example, with no 
                        extra parameters or packages included. ''',
    
    # Latex figure (float) alignment
    #
     #'figure_align': 'htbp',
     'figure_align': 'H',
     'fncychap':'\\usepackage[Glenn]{fncychap}',
     #Opciones de clase para latex para iniciar los caps en cualquier pagina(par e impar)
     #Mas opciones en -->
     #https://es.wikibooks.org/wiki/Manual_de_LaTeX/La_estructura_de_un_documento_en_LaTeX/Pre%C3%A1mbulo/Clases_de_documento
     'classoptions': ',openany'
}

############################################################################
############################# Elementos de la caratula #####################
############################################################################
import datetime
from babel.dates import format_date

#tituloTesina = ("Sistema para detección y reconocimiento de irregularidades sobre circuitos viales utilizando el sensor Kinect").decode("utf-8")
tituloTesina = ("SISTEMA PARA DETECCIÓN Y RECONOCIMIENTO DE IRREGULARIDADES SOBRE CIRCUITOS VIALES UTILIZANDO EL SENSOR KINECT").decode("utf-8")
# Imagen obtenida con graphics
autores = "Autores: Huincalef Rodrigo A. , Urrutia Guillermo G."
tutores = "Director de tesina: Ingravallo Gabriel"
facultad = "Facultad de ingeniería - Sede Trelew".decode("utf-8")

fecha  = datetime.date.today()
fechaActual = format_date(fecha, "d 'de' MMMM 'del' yyyy",locale='es').title()


universidad = "UNPSJB - Universidad Nacional de la Patagonia San Juan Bosco"
justificacion = """Tesina presentada a la Facultad de Ingeniería de la Universidad Nacional de la
Patagonia San Juan Bosco como parte de los requisitos para la obtención del título de Licenciado en Sistemas""".decode("utf-8")


latex_engine = 'lualatex'

# CAMPOS USADOS POR \FANCYHDR -->
#E: Even page
#O: Odd page
#L: Left field
#C: Center field
#R: Right field
#H: Header
#F: Footer
latex_elements['preamble'] += r"""
\usepackage{fancyhdr}
\usepackage[utf8]{inputenc}
\usepackage{amsfonts}
\usepackage{parskip}
\usepackage{amssymb}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{titlesec}
\usepackage{lmodern}
\usepackage{lastpage} 
\usepackage{color} 
\usepackage{etoolbox}
\usepackage[titles]{tocloft}
\usepackage{tikz}
\usepackage{fontspec}
%Paquete usado para la impresion de los numeros de capitulo
\usepackage{ifthen}
%\usepackage{calc}
\usepackage{pgf}
\usepackage{bm}
\usepackage{caption}
%\setmainfont{Linux Libertine Mono O}

% Sobreescritura de los comandos de latex generados por Sphinx automaticamente
\makeatletter
\setcounter{page}{5}

%Constante para la cantidad de capitulos previos a la introduccion,
%que no cuentan como capitulos enumerables en al tesis
%NOTA:Este valor se decrementa al valor \thechapter para comenzar
%numerando los contenidos de la tesina desde 1
%\def\cantCapitulosSinContenido{4}
\def\cantCapitulosSinContenido{3}



\definecolor{azul-oscuro}{RGB}{76, 85, 255}
\fancypagestyle{normal}{
    %Con este comando se limpia la configuracion para los encabezados por defecto
    \fancyhf{}
    
    \fancyfoot[LE,LO,RO,RE]{\center{\py@HeaderFamily\thepage}} % Cambio de footer
    %\fancyhead[RE,RO]{{\py@HeaderFamily \center{\rightmark} }} % Cambio de header
    
    \fancyhead[RE,RO]{ \center{ \begin{flushright} \textsl{\rightmark} \end{flushright}  }} % Cambio de header
    \renewcommand{\headrulewidth}{2pt}   % Definicion de las lineas de decorado encima
    \renewcommand{\headrule}{\hbox to\headwidth{%
        \color{azul-oscuro}\leaders\hrule height \headrulewidth\hfill}}

    \renewcommand{\footrulewidth}{0pt}   % y debajo de los encabezados y footers
}

%Cambiar el formato de las secciones, subsecciones y subsubsecciones
\definecolor{miazul}{RGB}{0,82,155}
\titleformat{\section}[block]{\Large\bfseries\sffamily\color{miazul}} 
              {\thesection.}{1pt}{}

\titleformat{\subsection}[block]{\Large\bfseries\sffamily\color{miazul}} 
              {\thesubsection.}{1pt}{}

\titleformat{\subsubsection}[block]{\Large\bfseries\sffamily\color{miazul}} 
              {\thesubsubsection.}{1pt}{}


% Se redefine el estilo de pagina "plain" usado por los comandos chapter,part y maketitle
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{ {\py@HeaderFamily\thepage} }
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}

\fancypagestyle{mi-toc}{%
  \fancyhf{}%
}
\tocloftpagestyle{mi-toc}
\pagestyle{normal}


%Definiendo variables y logueando a consola
%\def\foo{bar}
%\message{Imprimiendo el nombre del capitulo \the\foo}

% Los capitulos, secciones no numeradas llevan asterisco delante
%\chapter*{Acknowledgements}%

%Capitulos anteriores al contenido de la tesis (que no se numeran) 
%\def\capitulosgenerales{3}

%Numeros de capitulos que no deben ser numerados
\def\capAbstract{1}
\def\capReconocimientos{2}
\def\capResumen{3}
%\def\capOrganizacion{4}
\def\capBibliografia{8}


%A partir de la introduccion se comienzan a numerar los capitulos que son exclusivos
% de contenido de la tesina
\def\capIntroduccion{5}
%\pgfmathsetmacro{\var}{20 + 4}
%\message{Restando con PG : \var}  



%Definiendo macro para agregar el nombre de capitulo al principio 
\newcommand{\imprimirCapitulo}{
                \message{ Capitulo de contenido }
                \pgfmathsetmacro{\calcularCapitulo}{int(\thechapter - \cantCapitulosSinContenido) }
                \message{Restando con PG : \calcularCapitulo}  
                \node[
                    outer sep=0pt,
                    text width=2.5cm,
                    minimum height=3cm,
                    fill=myblue,
                    font=\color{white}\fontsize{80}{90}\selectfont,
                    align=center
                ] (num) {\calcularCapitulo};
                \node[
                    rotate=90,
                    anchor=south,
                    font=\color{black}\Large\normalfont
                ] at ([xshift=-5pt]num.west) {\textls[180]{\textsc{\chaptertitlename}}};
            }

% Removiendo el numero de capitulo del inicio de c/u
%\message{ Captiulos de contenido general: \capitulosgenerales  +++ }
\message{ Captiulos de contenido general: \cantCapitulosSinContenido  +++ }
\message{Antes del ifnum}
\titleformat{\chapter}[display]
{\normalfont\bfseries\color{myblue}}
 {\filleft
  \begin{tikzpicture}
      \message{Imprimiendo el nombre del capitulo \chaptertitlename : \thechapter : \value{chapter}--- }
      %Si el capitulo no es contenido general se lo imprime con el numero al inicio
      \ifthenelse{\thechapter=\capAbstract \OR \thechapter=\capReconocimientos \OR \thechapter=\capResumen \OR \thechapter=\capBibliografia}{ \message{No es capitulo contenido} }{\imprimirCapitulo}
  \end{tikzpicture}%
  }
{10pt}
{\titlerule[2.5pt]\vskip3pt\titlerule\vskip4pt\LARGE\sffamily}
[
\vspace{-0.5ex} 
\textcolor{myblue}{\rule{\textwidth}{0.9pt}}
]
%Redefiniendo los capitulos para eliminar el numero de capitulo
\renewcommand\thesection{\arabic{section}}        
%Identacion para cada parrafo
\setlength\parindent{1.7cm}
%Se sobreecribe el estilo por default del capitulo
\definecolor{myblue}{RGB}{0,82,155}

%Redefiniendo el toc(tabla de contenidos del documento)
\usepackage{titlesec}
\usepackage{titletoc}

%Directiva para el capitulo, seccion y subseccion del indice
\titlecontents{chapter}
              [0em]
              {\bfseries}
              {\hspace{1.5em}}
              {}
              {\hfill\contentspage}
\usepackage{appendix}
\renewcommand{\appendixname}{Anexos}
\usepackage{titletoc}

\usepackage[nottoc]{tocbibind}
\renewcommand{\listfigurename}{Indice de figuras}
\renewcommand{\listtablename}{Indice de tablas}
\usepackage{geometry}
\usepackage{pdflscape}

\makeatother
"""
#.. raw:: latex

#   \appendix
#   \noappendicestocpagenum
#   \addappheadtotoc
#   \settocdepth{chapter}



#TODO: Mirar en /usr/local/lib/python2.7/dist-packages/sphinx/writers/latex.py que es donde 
#genera el esqueleto del .tex principal


pathRaiz = os.getcwd()
imgPath = pathRaiz + "/figs/"
print "path:%s\n" % imgPath 
latex_elements['preamble'] += r'\graphicspath{ {%s} }' % imgPath


#% Cambiando el formato del inicio de los capitulos
#\titleformat{\chapter}[display]
#  {\normalfont\bfseries}{}{0pt}{\Large}   

# Extension instalada con $ sudo pip install sphinxcontrib-bibtex para soportar 
# el formato BibTex.
# #from docutils.parsers.rst import directives  # for Directive.option_spec
# #from sphinx.util.compat import Directive
# from docutils.parsers.rst import Directive, directives

mystyle = path + '//_estilos//title'

latex_elements['preamble'] += '\n'.join((
    r'\usepackage{%s}' % mystyle,
    r'\tituloTesina{%s}' % tituloTesina ,
    r'\autores{%s}' % autores ,
    r'\tutores{%s}' % tutores ,
    r'\facultad{%s}' % facultad,
    r'\universidad{%s}' % universidad,
    r'\justificacion{%s}' % justificacion,
    r'\fechaActual{%s}' % fechaActual
))


latex_additional_files += [mystyle + '.sty']

extensions = ['sphinxcontrib.bibtex','sphinx.ext.imgmath','sphinx.ext.numfig']
#extensions = ['sphinxcontrib.bibtex','sphinx.ext.imgmath']

numfig = True
numfig_number_figures = True
numfig_figure_caption_prefix = "Fig."

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    (master_doc, 'prueba.tex', '','', 'manual'),
#]


latex_documents = [
    (master_doc, 'Tesina-Huincalef-Urrutia.tex', '','', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Tesina-Huincalef-Urrutia', u'',
     [], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Tesina-Huincalef-Urrutia', u'prueba Documentation',
     author, 'Tesina-Huincalef-Urrutia', 'One line description of project.',
     'Miscellaneous'),
]



