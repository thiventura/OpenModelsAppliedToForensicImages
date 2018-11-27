# Open Models Applied To Forensic Images

## Apresentação
Esta ferramenta tem o intuito de auxiliar a análise forense de imagens. Ela foi feita utilizando o TensorFlow e utiliza de dois modelos existentes de deep learning para filtrar imagens relevantes para uma perícia.

## Modelos

### Open nsfw
O Yahoo liberou o seu [modelo](https://github.com/yahoo/open_nsfw) para detecção de pornografia. Como ela está em uma tecnologia diferente da utilizada nesta ferramenta, foi usada uma [outra implementação](https://github.com/mdietrichstein/tensorflow-open_nsfw). Este modelo estabele um score de imagem NSFW. Nesta ferramenta a imagem é considerada pornográfica se atinge um score maior que 80%.

### Inception
[ImageNet](http://www.image-net.org/) é um banco de dados de imagens que é constantemente utilizado em competições de classificações de imagens. Diversos modelos já foram criados tendo como referência classes existentes nesta base. Um modelo disponível é o [Inception](https://github.com/tensorflow/models/tree/master/research/inception). Este modelo está preparado para classificar 1000 classes diferentes, no qual IDs específicos foram selecionados para representar imagens relevantes para a perícia. Em `docs/imagenet.xlsx` contém todas as classes do modelo e quais estão sendo consideradas.


## Funcionamento
![Fluxograma](https://github.com/thiventura/OpenModelsAppliedToForensicImages/blob/master/docs/FluxoOpenModelsForensicImages.png)


## Uso da ferramenta

### Requisitos
* Python 3.6
* Tensorflow 1.5
* Baixe os modelos [Inception v2](https://drive.google.com/file/d/1Tnju6JpV_KUnMsi544jXReb30MAAzmk5/view?usp=sharing) e [Open nsfw](https://drive.google.com/file/d/13xHu_B4_Yw9f6XPx8oDu6Idc7WaaR_bh/view?usp=sharing) e coloque-os na pasta `models`

### Classificação
A classificação das imagens é feita por meio do arquivo `src/evaluate_images.py`. Há 2 parâmetros obrigatórios:
* images_dir: pasta que contém todas as imagens a serem analisadas
* details_dir: pasta em que as imagens serão movidas, organizadas em subpastas.

Exemplo de uso:

    python evaluate_images.py --images_dir ../test/imagens/ --details_dir ../test/imagens_filtradas/
