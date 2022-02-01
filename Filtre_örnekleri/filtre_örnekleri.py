import cv2
import numpy as np
#OpenCV filtre örnekleri
resim = cv2.imread(r"opencv\video_ve_resimler\taylor.jpg")
gri_resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

while True:
    print("1-Canny 2-Gauss 3-Medyan 4-Bileteral 5-Keskinlestirme 6-Kendi filtremiz 7-Laplace 8-Sobel 9-Cikis")
    secim = input("Yapmak istediginiz islemi seciniz: ")
    
    match secim:
        case '1':
            #canny kenar bulma filtresi ,  threshold : eşik değeri
            kenar = cv2.Canny(gri_resim,50,100)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Canny",kenar)
            cv2.waitKey(0)
        case '2':
            #gauss bulanıklaştırma filtresi , ksize pozitif ve tek sayı olmak zorunda
            bulanik = cv2.GaussianBlur(resim,(7,7),0)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Gauss",bulanik)
            cv2.waitKey(0)
        case '3':
            #medyan gürültü azaltma filtresi
            medyan = cv2.medianBlur(resim,3)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Medyan",medyan)
            cv2.waitKey(0)
        case '4':
            #bilateral gürültü azaltma ve yumuşatma filtresi , sigmacolor arttıkça görüntü yumuşar
            bilateral = cv2.bilateralFilter(resim,15,45,65)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Bilateral",bilateral)
            cv2.waitKey(0)
        case '5':
            #keskinleştirme filtresi ,  aşağıdaki filtre kullanılan temel keskinleştirme filtrelerinden biri

            filter = np.array( [[-1,-1,-1],
                                [-1, 9,-1],
                                [-1,-1,-1]])
            #buradaki -1 resmin veri tipinin değişmemesi için (float,int)
            dst = cv2.filter2D(resim,-1,filter)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Keskin",dst)
            cv2.waitKey(0)
        case '6':
            #kendi filtremizi oluşturma
            random_filter = np.array( [[-4,7,-1],
                                       [-2,8,3],
                                       [-9,1,2]])

            dst2 = cv2.filter2D(resim,-1,random_filter)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Random",dst2)
            cv2.waitKey(0)
        case '7':
            #Laplace kenar bulma filtresi , ksize = işlemi yapacak matrisin boyutu(tek sayı olmak zorunda)
            laplace = cv2.Laplacian(gri_resim,-1,ksize=3)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Laplace",laplace)
            cv2.waitKey(0)
        case '8':
            #sobel kenar bulma  filtresi 
            sobel = cv2.Sobel(gri_resim,-1,1,1,ksize=5)
            cv2.imshow("Orjinal",resim)
            cv2.imshow("Sobel",sobel)
            cv2.waitKey(0)
        case '9':
            break
            
    cv2.destroyAllWindows()
