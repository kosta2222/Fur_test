using System;
// using AForge.Math;
// class Complex{
// public double re;
// public double im;
//  public Complex( double re, double im ) 
//  {
//             this.re = re;
//             this.im = im;
//  }
// public override string ToString(){
//     return $"{this.re}+{this.im}j";
// }

// }

namespace My_third_arr
{
    class Program
    {
        static void Main(string[] args)
        {
          Complex k= new Complex(7,0); 
          Complex[] data={new Complex(17,0),new Complex(9,0),new Complex(10,0)};  
          Complex[] out_= Program.DFT(data, 1);
          for(int i=0;i<out_.Length;i++)
            Console.WriteLine(out_[i]); 
            
        }
    public static Complex[] DFT( Complex[] data, int direction )
		{
			int			n = data.Length;
			double		arg, cos, sin;
			Complex[]	dst = new Complex[n];

			// for each destination element
			for ( int i = 0; i < n; i++ )
			{
				dst[i] =new Complex(0,0);

				arg = - (int) direction * 2.0 * System.Math.PI * (double) i / (double) n;

				// sum source elements
				for ( int j = 0; j < n; j++ )
				{
					cos = System.Math.Cos( j * arg );
					sin = System.Math.Sin( j * arg );

					dst[i].Re += ( data[j].Re * cos - data[j].Im * sin );
					dst[i].Im += ( data[j].Re * sin + data[j].Im * cos );
				}
      }
          
    	 	 
     return dst;
    }
   
  }
}


