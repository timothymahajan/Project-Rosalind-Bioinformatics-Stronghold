/*
Problem 1: Counting DNA Nucleotides
Given: A DNA string ss of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ProjectRosalindcs
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine(DNA("CTACGAAAAAAGATGTCGACTGGGATTTAGGTGGGACAATCAGTGTGTATGTACTGTCTCAGTGTGCGTAGCCACTCATTCATTCAATCCAATCCTCTTGGACCATCACCTATCAAGCTCGTTTACCGGGATGTACGTGCCCCCTGAGCCACATCTGTGACAAGGAACCTCTAGCCTACTACAGATAAGAAGGGGCATGGCCGGGACCGAAGGGCCGCACAATATCAACGGTGCACAAGTGCAAACGACCCAGTCTAAGTACCAGCCGCGCTTCAGTTACCGTCTCACCCTAAGCTCTATACGTGGGTTGAAACGTCGGCGTACCTCACCTGCTGAGGGGGGGTTGTGGTCTTATCTGCTGCAGAGGAGGCTAACTCTGCGTGTTCTGGTCGGTAGGTGGGTAATAAGGAGACAAGTCACATGCTAGTTGATGACTAGGATCCCGGTAACCTTGGTGCCCAATCTTAGTGACGTTAAGGAACGCATGCAATTGTCGGGGCGGCTTTGCAGTTAAAGCTTGATAAGGGAGCGATAAACCTTGGGTGTCCGCAAATTAGAAGACTCTAGAGCATCCACGGCGCATTATTTACGGTATTTCAGGACTAGGAGAGCTATTTCGCGAAGAAAATAACGCGCGGGGATCTTTTATACTTATTGCCTAGCATCCTTTAGACGATAGGTCCGTACCTTCGAGTACGTGGTGAACTTTATTTTAGGTTCCGTCAGCATGCGCTGACAGTAGGCTCTTTTACATTGATTAACTAGGATTCGCAGGCCGTCGGATGGAAGTTGAGAGAGAGGATA"));
            Console.ReadLine();
        }

        static string DNA(string strDna)
        {
            StringBuilder sb = new StringBuilder();
            List<string> nucleotides = new List<string>() { "A", "C", "G", "T" };
            foreach (string nucleotide in nucleotides)
            {
                sb.Append(strDna.Length - strDna.Replace(nucleotide, string.Empty).Length).ToString();
                sb.Append(" ");
            }
            return sb.ToString().TrimEnd();
        }
    }
}
