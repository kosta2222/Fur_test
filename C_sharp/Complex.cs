class Complex{
public double Re;
public double Im;
 public Complex( double re, double im ) 
 {
            this.Re = re;
            this.Im = im;
 }
public override string ToString(){
    return $"{this.Re}+{this.Im}j";
}

}