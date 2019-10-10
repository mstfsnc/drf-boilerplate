# drf-boilerplate
django rest framework kullanım için hazır araç gereç ve örnek bir blog uygulaması

## Neler var
* Arkayüzde için django, django-rest-framework, postgresql
* Önyüz için webpack
* Geliştirme ve canlı ortam için docker

### Kurulum
İnternet yavaş olduğu için imajı dockera pushlayamadım. O yüzden lokalde build etmelisiniz.

```
cp .env.example .env
make bundle && make build
```

### Çalıştırma
Geliştirme ortamı (attach)
```
make development 
```

Canlı ortam (nginx)
```
make production 
```