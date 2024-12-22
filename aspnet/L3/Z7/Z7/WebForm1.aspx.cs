using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Xml.Linq;

namespace Z7
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void ButtonUpload_Click(object sender, EventArgs e)
        {
            // Sprawdzamy, czy plik został przesłany
            if (FileUpload1.HasFile)
            {
                // Pobieramy dane o pliku
                string fileName = FileUpload1.FileName;
                int fileSize = FileUpload1.PostedFile.ContentLength;

                // Odczytujemy zawartość pliku binarnie
                byte[] fileBytes = FileUpload1.FileBytes;

                // Obliczamy sumę bajtów modulo 0xFFFF
                int checksum = fileBytes.Sum(b => (int)b) % 0xFFFF;

                // Generujemy XML z opisem pliku
                XDocument xmlDoc = new XDocument(
                    new XElement("opis",
                        new XElement("nazwa", fileName),
                        new XElement("rozmiar", fileSize.ToString()),
                        new XElement("sygnatura", checksum.ToString())
                    )
                );

                // Konwertujemy dokument XML na string
                string xmlString = xmlDoc.ToString();

                // Ustawiamy nagłówki odpowiedzi, aby przeglądarka wywołała okno "Otwórz/Zapisz/Anuluj"
                /*Response.Clear();
                Response.ContentType = "application/xml";
                Response.AddHeader("Content-Disposition", $"attachment; filename=opis_{fileName}.xml");
                Response.ContentEncoding = System.Text.Encoding.UTF8;

                // Wysyłamy zawartość XML jako odpowiedź
                Response.Write(xmlString);
                Response.End();*/
                Response.Clear();
                Response.ContentType = "application/xml";


                string encodedFileName = Uri.EscapeDataString(fileName); // RFC5987
                string header = $"attachment; filename=\"{fileName}\"; filename*=UTF-8''{encodedFileName}"; // jeśli nie obsługuje, mamy fallback

                Response.AddHeader("Content-Disposition", header); // content-disposition attachment/inline zdecyduje jak ma być potraktowany plik przez przegladarke
                Response.Write(xmlString);
                Response.End();
            }
            else
            {
                // W przypadku braku pliku wyświetlamy komunikat
                Response.Write("Proszę wybrać plik do przesłania.");
            }
        }
    }
}