#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, re

#css_combined = urllib2.urlopen("http://atomeye.com/assets/css_combined/style.css_combined").read()
#css_combined = urllib2.urlopen("http://localhost/css_combined-dig/test/ink.css_combined").read()

css_combined = '''
@font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-Light"), url("sourcesanspro-light-webfont.svg") format("svg"), url("sourcesanspro-light-webfont.woff") format("woff"), url("SourceSansPro-Light.otf") format("opentype"); font-weight: 300; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-LightIt"), url("sourcesanspro-lightit-webfont.svg") format("svg"), url("sourcesanspro-lightit-webfont.woff") format("woff"), url("SourceSansPro-LightIt.otf") format("opentype"); font-weight: 300; font-style: italic; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-Regular"), url("sourcesanspro-regular-webfont.svg") format("svg"), url("sourcesanspro-regular-webfont.woff") format("woff"), url("SourceSansPro-Regular.otf") format("opentype"); font-weight: 400; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-It"), url("sourcesanspro-it-webfont.svg") format("svg"), url("sourcesanspro-it-webfont.woff") format("woff"), url("SourceSansPro-It.otf") format("opentype"); font-weight: 400; font-style: italic; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-Semibold"), url("sourcesanspro-semibold-webfont.svg") format("svg"), url("sourcesanspro-semibold-webfont.woff") format("woff"), url("SourceSansPro-Semibold.otf") format("opentype"); font-weight: 600; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-SemiboldIt"), url("sourcesanspro-semiboldit-webfont.svg") format("svg"), url("sourcesanspro-semiboldit-webfont.woff") format("woff"), url("SourceSansPro-SemiboldIt.otf") format("opentype"); font-weight: 600; font-style: italic; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-Bold"), url("sourcesanspro-bold-webfont.svg") format("svg"), url("sourcesanspro-bold-webfont.woff") format("woff"), url("SourceSansPro-Bold.otf") format("opentype"); font-weight: 700; } @font-face { font-family: "Source Sans Pro"; src: local("SourceSansPro-BoldIt"), url("sourcesanspro-boldit-webfont.svg") format("svg"), url("sourcesanspro-boldit-webfont.woff") format("woff"), url("SourceSansPro-BoldIt.otf") format("opentype"); font-weight: 700; font-style: italic; } @font-face { font-family: "Meta Serif Office Pro"; src: local("MetaSerifOffcPro-Book"), url("MetaSerifWebPro-Book.woff") format("woff"); font-weight: 400; } @font-face { font-family: "Meta Serif Office Pro"; src: local("MetaSerifOffcPro-BookItalic"), url("MetaSerifWebPro-BookItalic.woff") format("woff"); font-weight: 400; font-style: italic; } @font-face { font-family: "Meta Serif Office Pro"; src: local("MetaSerifOffcPro-Bold"), url("MetaSerifWebPro-Bold.woff") format("woff"); font-weight: 700; } @font-face { font-family: "Meta Serif Office Pro"; src: local("MetaSerifOffcPro-BoldItalic"), url("MetaSerifWebPro-BoldItalic.woff") format("woff"); font-weight: 700; font-style: italic; } @font-face { font-family: "Tisa Mobile Pro"; src: local("TisaMobiPro"), url("TisaWebPro.woff") format("woff"); font-weight: 400; } @font-face { font-family: "Tisa Mobile Pro"; src: local("TisaMobiPro-Italic"), url("TisaWebPro-Italic.woff") format("woff"); font-weight: 400; font-style: italic; } @font-face { font-family: "Tisa Mobile Pro"; src: local("TisaMobiPro-Bold"), url("TisaWebPro-Bold.woff") format("woff"); font-weight: 700; } @font-face { font-family: "Tisa Mobile Pro"; src: local("TisaMobiPro-BoldItalic"), url("TisaWebPro-BoldItalic.woff") format("woff"); font-weight: 700; font-style: italic; } @font-face { font-family: 'Chronicle'; src: local("MetaSerifOffcPro-Book"), url("MetaSerifWebPro-Book.woff") format("woff"); font-weight: 400; } @font-face { font-family: 'Chronicle'; src: local("MetaSerifOffcPro-BookItalic"), url("MetaSerifWebPro-BookItalic.woff") format("woff"); font-weight: 400; font-style: italic; } @font-face { font-family: 'Chronicle'; src: local("MetaSerifOffcPro-Bold"), url("MetaSerifWebPro-Bold.woff") format("woff"); font-weight: 700; } @font-face { font-family: 'Chronicle'; src: local("MetaSerifOffcPro-BoldItalic"), url("MetaSerifWebPro-BoldItalic.woff") format("woff"); font-weight: 700; font-style: italic; } @font-face { font-family: 'Whitney'; src: local("SourceSansPro-Regular"), url("sourcesanspro-regular-webfont.svg") format("svg"), url("sourcesanspro-regular-webfont.woff") format("woff"), url("SourceSansPro-Regular.otf") format("opentype"); font-weight: 400; } @font-face { font-family: 'Whitney'; src: local("SourceSansPro-It"), url("sourcesanspro-it-webfont.svg") format("svg"), url("sourcesanspro-it-webfont.woff") format("woff"), url("SourceSansPro-It.otf") format("opentype"); font-weight: 400; font-style: italic; } @font-face { font-family: 'Whitney'; src: local("SourceSansPro-Regular"), url("sourcesanspro-regular-webfont.svg") format("svg"), url("sourcesanspro-regular-webfont.woff") format("woff"), url("SourceSansPro-Regular.otf") format("opentype"); font-weight: 500; } @font-face { font-family: 'Whitney'; src: local("SourceSansPro-It"), url("sourcesanspro-it-webfont.svg") format("svg"), url("sourcesanspro-it-webfont.woff") format("woff"), url("SourceSansPro-It.otf") format("opentype"); font-weight: 500; font-style: italic; } @font-face { font-family: 'Whitney'; src: local("SourceSansPro-Semibold"), url("sourcesanspro-semibold-webfont.svg") format("svg"), url("sourcesanspro-semibold-webfont.woff") format("woff"), url("SourceSansPro-Semibold.otf") format("opentype"); font-weight: 600; } @font-face { font-family: "Whitney"; src: local("SourceSansPro-SemiboldIt"), url("sourcesanspro-semiboldit-webfont.svg") format("svg"), url("sourcesanspro-semiboldit-webfont.woff") format("woff"), url("SourceSansPro-SemiboldIt.otf") format("opentype"); font-weight: 600; font-style: italic; } @font-face { font-family: "Whitney"; src: local("SourceSansPro-Bold"), url("sourcesanspro-bold-webfont.svg") format("svg"), url("sourcesanspro-bold-webfont.woff") format("woff"), url("SourceSansPro-Bold.otf") format("opentype"); font-weight: 700; } @font-face { font-family: "Whitney"; src: local("SourceSansPro-BoldIt"), url("sourcesanspro-boldit-webfont.svg") format("svg"), url("sourcesanspro-boldit-webfont.woff") format("woff"), url("SourceSansPro-BoldIt.otf") format("opentype"); font-weight: 700; font-style: italic; } @font-face { font-family: 'WhitneyMed'; src: local("SourceSansPro-Regular"), url("sourcesanspro-regular-webfont.svg") format("svg"), url("sourcesanspro-regular-webfont.woff") format("woff"), url("SourceSansPro-Regular.otf") format("opentype"); font-weight: 500; } @font-face { font-family: 'WhitneyMed'; src: local("SourceSansPro-It"), url("sourcesanspro-it-webfont.svg") format("svg"), url("sourcesanspro-it-webfont.woff") format("woff"), url("SourceSansPro-It.otf") format("opentype"); font-weight: 500; font-style: italic; } @font-face { font-family: 'WhitneySemi'; src: local("SourceSansPro-Semibold"), url("sourcesanspro-semibold-webfont.svg") format("svg"), url("sourcesanspro-semibold-webfont.woff") format("woff"), url("SourceSansPro-Semibold.otf") format("opentype"); font-weight: 600; } @font-face { font-family: 'WhitneySemi'; src: local("SourceSansPro-SemiboldIt"), url("sourcesanspro-semiboldit-webfont.svg") format("svg"), url("sourcesanspro-semiboldit-webfont.woff") format("woff"), url("SourceSansPro-SemiboldIt.otf") format("opentype"); font-weight: 600; font-style: italic; } html, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video { margin: 0; padding: 0; border: 0; vertical-align: baseline; } article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section { display: block; } body { margin: 0; padding: 0; } ol, ul, li { list-style: none; } blockquote, q { quotes: none; } blockquote:before, blockquote:after, q:before, q:after { content: ''; content: none; } table { border-collapse: collapse; border-spacing: 0; } html { font-size: 10px; } body { background-color: #faf9f8; background-image: url('../images/background_tile.png?version=1370454284'); font-family: "Source Sans Pro", "Lucida Grande", Verdana, Helvetica, sans; font-weight: 400; font-size: 1.6rem; line-height: 2rem; } .ie8 body { font-size: 16px; line-height: 20px; } a { color: inherit; text-decoration: none; } a:hover { color: #0091b2; } em { font-style: italic; } #main > img { display: none; } ol { list-style-type: decimal; padding-left: 2rem; margin: 2.0rem 0; } .ie8 ol { padding-left: 20px; margin: 20px 0; } .clear { clear: both; } p { font-family: "Source Sans Pro", "Lucida Grande", Verdana, Helvetica, sans; font-weight: 400; font-size: 1.4rem; } .ie8 p { font-size: 14px; } small { font-size: 1.3rem; text-transform: uppercase; } .ie8 small { font-size: 13px; } strong { font-weight: 600; } sub { line-height: normal; font-family: "Source Sans Pro", "Lucida Grande", Verdana, Helvetica, sans; font-weight: 400; font-size: 1rem; font-size: 1rem; vertical-align: super; } .ie8 sub { font-size: 10px; } .ie8 sub { font-size: 10px; } sup { line-height: 1em; font-size: 1rem; vertical-align: sub; } .ie8 sup { font-size: 10px; } table { width: 100%; font-size: 1.4rem; border: none; margin: 1em 0; } .ie8 table { font-size: 13px; } table tbody tr td { border: 1px solid #ddd; } table thead tr td, table tbody tr td, table tfoot tr td { background: transparent; } table thead tr td { font-weight: 700; } table td { padding: 1rem 1.5rem; text-transform: none; letter-spacing: inherit; font-weight: 400; } .ie8 table { padding: 10px 15px; } table tfoot td { font-size: 1.3rem; } .ie8 table { padding: 10px 15px; } ul { list-style-type: disc; padding-left: 2rem; margin: 2.0rem 0; } .ie8 ul { padding-left: 20px; margin: 20px 0; } .ie8 label { display: block; } .hidden { display: none; } .input[type='button'], .input[type='submit'] { -webkit-border-radius: 2px; -moz-border-radius: 2px; -ms-border-radius: 2px; -o-border-radius: 2px; border-radius: 2px; -webkit-appearance: none; -moz-appearance: none; -ms-appearance: none; -o-appearance: none; appearance: none; } input, textarea { -webkit-appearance: none; -webkit-border-radius: 0; } input[type="checkbox"] { -webkit-appearance: checkbox; } div.overlay { position: fixed; top: 0px; bottom: 0px; left: 0px; right: 0px; z-index: 99; background-color: rgba(255, 255, 255, 0); -webkit-transition-property: background-color; -moz-transition-property: background-color; -ms-transition-property: background-color; -o-transition-property: background-color; transition-property: background-color; -webkit-transition-duration: 0.25s; -moz-transition-duration: 0.25s; -ms-transition-duration: 0.25s; -o-transition-duration: 0.25s; transition-duration: 0.25s; -webkit-transition-timing-function: ease-out; -moz-transition-timing-function: ease-out; -ms-transition-timing-function: ease-out; -o-transition-timing-function: ease-out; transition-timing-function: ease-out; } div.overlay.displayed { display: block; } @media only screen and (min-width: 320px) and (max-width: 480px) { div.overlay { position: absolute; } } div.overlay.visible { background-color: rgba(255, 255, 255, 0.75); } div.overlay.visible .modal-container { -webkit-transform: translateY(0px); -moz-transform: translateY(0px); -ms-transform: translateY(0px); -o-transform: translateY(0px); transform: translateY(0px); } .ie7 div.overlay, .ie8 div.overlay, .ie9 div.overlay { opacity: 0; background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA2hpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYxIDY0LjE0MDk0OSwgMjAxMC8xMi8wNy0xMDo1NzowMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpENEQ1QkNDNDFCMjA2ODExOEMxNEVCRUVFRTBBOTRFRSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDowNjZFMjEzOUMzQTIxMUUxQTgxNEJEOUY5QTQ5RkU1QyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDowNjZFMjEzOEMzQTIxMUUxQTgxNEJEOUY5QTQ5RkU1QyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M2IChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ODA4QzVCQzEzNTIwNjgxMTgwODNDN0Y2RTMxNTJCNjEiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6RDRENUJDQzQxQjIwNjgxMThDMTRFQkVFRUUwQTk0RUUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz76KILoAAAAG0lEQVR42mL8////TQYiABMDkWBUIXUUAgQYAC1WA+qNAnyEAAAAAElFTkSuQmCC'); } .ie7 div.overlay.visible, .ie8 div.overlay.visible, .ie9 div.overlay.visible { opacity: 1; } div.modal-container { position: relative; width: 300px; min-height: 300px; margin: 0 auto; margin-top: 100px; -webkit-border-radius: 2px; -moz-border-radius: 2px; -ms-border-radius: 2px; -o-border-radius: 2px; border-radius: 2px; -webkit-box-shadow: 0px 2px 10px #888888; -moz-box-shadow: 0px 2px 10px #888888; box-shadow: 0px 2px 10px #888888; font-family: "Source Sans Pro", "Lucida Grande", Verdana, Helvetica, sans; font-weight: 500; font-size: 1.2rem; color: #999; overflow: hidden; background-color: white; -webkit-transform: translateY(700px); -moz-transform: translateY(700px); -ms-transform: translateY(700px); -o-transform: translateY(700px); transform: translateY(700px); -webkit-transition-property: -webkit-transform; -moz-transition-property: -moz-transform; -ms-transition-property: -ms-transform; -o-transition-property: -o-transform; transition-property: transform; -webkit-transition-duration: 0.25s; -moz-transition-duration: 0.25s; -ms-transition-duration: 0.25s; -o-transition-duration: 0.25s; transition-duration: 0.25s; -webkit-transition-timing-function: ease-out; -moz-transition-timing-function: ease-out; -ms-transition-timing-function: ease-out; -o-transition-timing-function: ease-out; transition-timing-function: ease-out; } .ie8 div.modal-container { font-size: 12px; } @media only screen and (min-width: 320px) and (max-width: 480px) { div.modal-container { -webkit-box-shadow: 0px 2px 10px #888888; -moz-box-shadow: 0px 2px 10px #888888; box-shadow: 0px 2px 10px #888888; width: 100%; margin: 0px; } } div.modal-container.dark { background-color: black; } div.modal-container.dark .close-button { background-image: url('../images/modal-close-button.png?version=1370454284'); background-repeat: no-repeat; width: 36px; height: 35px; right: 5px; top: 5px; } @media only screen and (-webkit-min-device-pixel-ratio: 2) { div.modal-container.dark .close-button { -webkit-background-size: 35px auto; -moz-background-size: 35px auto; -o-background-size: 35px auto; background-size: 35px auto; background-image: url('../images/modal-close-button@2x.png?version=1370454284'); } } div.modal-container.dark .close-button:hover { background-position-y: -33px; } div.modal-container.dark .close-button:active { background-position-y: -66px; } div.modal-container.promo { width: 700px; } div.modal-container.screenshot { width: 98%; max-width: 800px; margin-top: 30px; padding: 20px; } @media only screen and (min-width: 320px) and (max-width: 480px) { div.modal-container.screenshot { width: 100%; margin-top: 0px; min-width: 767px; } } div.modal-container.screenshot .descriptions { margin: 0px; padding: 0px; margin-top: 13px; width: 38%; font-size: 14px; line-height: 17px; } div.modal-container.screenshot .screenshot-wrapper { width: 60%; } div.modal-container.video { width: 680px; } @media all and (device-width: 768px) and (device-height: 1024px) { div.modal-container.has-focus .content { max-height: 400px; overflow-y: scroll; } } div.modal-container .validation-failed { color: #C1272D !important; border: 1px solid red !important; }

'''

css_combined = re.sub( r'\s+', ' ', css_combined )
css_combined = re.sub(r'([a-zA-Z0-9])\s*?}', r'\g<1>'+';}', css_combined )
css_combined = re.sub(r'({)', r'\g<1>'+'\n', css_combined )
css_combined = re.sub(r'(;)', r'\g<1>'+'\n', css_combined )
css_combined = re.sub(r'(.*;)', r'\t'+'\g<1>', css_combined )
css_combined = re.sub(r'(})', r'\g<1>'+'\n', css_combined )

print css_combined
