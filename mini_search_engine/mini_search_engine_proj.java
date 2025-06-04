import java.util.Scanner;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class mini_search_engine_proj {
    private StringHashTable hashtable;  
    
    public mini_search_engine_proj() {
        hashtable = new StringHashTable();  // initialize
    }

    public static void main(String[] args) {
        mini_search_engine_proj search_engine = new mini_search_engine_proj();
    
        try {
            // time it takes to read files
            long startReadFile = System.nanoTime();
            search_engine.readFile();
            double readTime = (System.nanoTime() - startReadFile) / 1000000.0; // get time in milliseconds
            // print the time it takes to read files
            System.out.printf("Time it takes to read files: %.2fms\n", readTime);
            search_engine.searchAgain();

        } catch (Exception ex) {
            System.err.println("There was an error in reading files: " + ex.getMessage());
        }
    }

    // function for user query input and finding match in documents
    public void search(Scanner scan) {
        System.out.print("Search: ");
        String query = scan.nextLine().toLowerCase().trim().replaceAll("\\s+", " ");
        // check if query is empty
        if (query.isEmpty()) {
          System.out.println("Query is empty.");
          return;
        }
       // prevent AND and OR in the same query
       boolean containsOr = query.contains(" or ");
       boolean containsAnd = query.contains(" and ");
       if (containsAnd && containsOr) {
        System.out.println(" Invalid input. Cannot mix AND and OR");
        return;
       }
       // error handling for incorrectly used boolean operators
       if(query.startsWith("and ") || query.startsWith("or ")
       || query.endsWith(" and") || query.endsWith(" or")
       || query.equals("and") || query.equals("or")) {
        System.out.println("Query is invalid, cannot start or end with AND or OR");
        return;
       } 

      // error handling for instances such as word1ANDword2
      String [] queryParts = query.split("\\s+"); // split query on whitespace
      for (int i = 0; i < queryParts.length; i++)  {
        String queryPart = queryParts[i];
        if (queryPart.equalsIgnoreCase("and") || queryPart.equalsIgnoreCase("or")) {
          // check if adjacent query elements are valid
          if ((i > 0 && queryParts[i-1].isEmpty()) ||(i < queryParts.length && queryParts[i+1].isEmpty())) {
            System.out.println("Query is invalid");
            return;
          }
        }
      }

       
       // split AND and OR from the rest of the query
       String [] queryElements;
       String booleanOperator = ""; // check for AND and OR

       if (containsAnd) {
        booleanOperator = "AND";
        queryElements = query.split(" and "); // remove AND from searched words
       }
       else if (containsOr) {
        booleanOperator = "OR";
        queryElements = query.split(" or "); // remove OR from searched words
       }
       else {
        booleanOperator = "NONE";
        queryElements = new String[]{query}; // create a string array containing one element (query)
       }

       // error handling if two boolean operators are inputted consecutively
       for (String queryElement : queryElements) {
        if (queryElement.equals("and") || queryElement.equals("or")) {
          System.out.println("Query invalid. There are consecutive boolean operators");
          return;
        }
       }

       // check if all query elements are valid
       for (String queryElement : queryElements) {
        if (queryElement.isEmpty() || !queryElement.matches("[a-z0-9]+")) {
          System.out.println("Query is invalid");
          return;
        }
       }

       // initialize start time for query search
       long searchStartTime = System.nanoTime();

       // query processing
       String [] resultingDocuments = getDocumentsContainingQuery(queryElements[0]);
       for (int i = 1; i < queryElements.length; i++) {
        String [] nextDocuments = getDocumentsContainingQuery(queryElements[i]);
        if (booleanOperator.equals("AND")) {
          resultingDocuments = getIntersection(resultingDocuments, nextDocuments);
        }
        else if (booleanOperator.equals("OR")) {
          resultingDocuments = getUnion(resultingDocuments, nextDocuments);
        }
       }

       // calculate the search time
       double searchTime = (System.nanoTime() - searchStartTime) / 1000000.0; // get search time in milliseconds
       
       // show results with the time it takes to process the query
       System.out.print( "\"" + queryElements[0] + "\""); 
       for (int i = 1; i < queryElements.length; i ++) {
        System.out.print(" " + booleanOperator + " \"" + queryElements[i] + "\"");
       }
       System.out.print(" found in: \n");

      if (resultingDocuments.length == 0 || resultingDocuments[0] == null) {
        System.out.println("No results were found");
      }
      else {
        for (String document : resultingDocuments) {
          if (document != null) System.out.println(" " + document);
        }
      }
      // display runtime for the search operation
       System.out.printf("\nQuery was processed in: %.2fms\n", searchTime);
    }

  // function asking the user if they want to search again
    public void searchAgain () {
      Scanner scan = new Scanner(System.in);
      String option;
      try {
        do {
          search(scan);

          System.out.print("Do you want to search again? (yes or no) ");
          option = scan.nextLine().trim().toLowerCase();

          while (!option.equals("yes") && !option.equals("no")) {
            System.out.print("Input is invalid. Please enter 'yes or 'no only: ");
            option = scan.nextLine().trim().toLowerCase();
          }
        } while (option.equals("yes"));
        System.out.println("Exiting program...");
      } finally {
        scan.close();
      }
    }

    public String [] getDocumentsContainingQuery (String word) {
      int index = hashtable.hashFunction(word);
      while(hashtable.hashTable[index] != null) {
        if ( hashtable.hashTable[index].key.equals(word)) {
          return hashtable.hashTable[index].documents;
      }
      index = (index + 1) % hashtable.SIZE;
      }
      return new String[0];
    } 

    // function to get common words between documents (for AND operator)
    public String[] getIntersection(String[] a, String[] b) {
      String[] result = new String [5]; // initialize array to store intersection
      int counter = 0; // counter to keep track of common documents
      // check each document, then compare if there are common words
      for (String docA: a) {
        if (docA == null) continue; // skip null entries
        for (String docB : b) {
          if (docB == null) continue; // skip null entries
          if (docA.equals(docB)) {
            result[counter] = docA;
            counter = counter + 1;
            break; // exit loop if there is common document
          }
        }
      }
      return result; // gets the array of common documents
    }

    // function to get union of two sets of documents (for OR operator)
    public String [] getUnion(String [] a, String[] b) {
      String [] result = new String [10];  // initialize array to store union
      int counter = 0;
      // check all documents from first array
      for (String doc : a) {
      if (doc != null) result[counter++] = doc;
      }
      // add elements in other array that does not exist in first array
      for (String doc : b) {
      if (doc == null) continue;  // skip null entries
      boolean inResult = false;
      // check if a document is already in the result
      for (int i = 0; i < counter; i++) {
        if(doc.equals(result[i])) {
        inResult = true;
        break;
        }
      }
      // add document, if not in the result
      if (!inResult) result[counter++] = doc;
      }
      return result;  // return union of array of documents
    }

    // create class for hashtable inputs
    class HashInput {
        String key; // key represents the parsed word
        String documents[]; // contains the names of the documents
        int docuCount;

        public HashInput(String key) {
            this.key = key;
            this.documents = new String[5];
            this.docuCount = 0;
        }
    }

    // hashtable class
    public class StringHashTable {
        // create a node for making a linked list in each bucket
        private final int SIZE = 157; // use prime number as size of hashtable for better distribution
        private HashInput[] hashTable = new HashInput[SIZE]; // initializes hashtable as an array of hash inputs

        // HASH FUNCTION
        private int hashFunction(String word) {
            int hash = 0;
            for (char c : word.toCharArray()) {
                hash = (37 * hash + c) % SIZE;
            }
            return hash;
        }

        // function for putting read words into hashtable
        public void putToHashTable(String word, String document) {
            int index = hashFunction(word);
            // check whether a bucket is occupied or is not the same word as the query
            // continues while current bucket is not empty and the current word does not match the query
            while (hashTable[index] != null && !hashTable[index].key.equals(word)) {
                index = (index + 1) % SIZE; // implementing linear probing
            }
            // if a certain index is empty, put the word there
            if (hashTable[index] == null) {
                hashTable[index] = new HashInput(word);
            }

            // check if the word is contained in a document
            // if word is contained in the document, add it
            for (int i = 0; i < hashTable[index].docuCount; i++) {
                if (hashTable[index].documents[i].equals(document)) {
                    return; // The method returns if word is already found in the document, to prevent duplicates
                }
            }
            if (hashTable[index].docuCount < hashTable[index].documents.length) {
                hashTable[index].documents[hashTable[index].docuCount++] = document;
            }
        }
    }

    // function for parsing words in files then puts the words into the hashtable
    public void readFile() throws IOException {
        String[] documents = {"Doc1.txt", "Doc2.txt", "Doc3.txt"};
        for (String doc : documents) {
            try (BufferedReader reader = new BufferedReader(new FileReader(doc))) {
                String line;
                // read each line
                while ((line = reader.readLine()) != null) {
                  // words are converted to lowercase and splits them every time a non-word character appears
                    String[] words = line.toLowerCase().split("\\W+");
                    for (String word : words) {
                        if (!word.isEmpty()) {
                            hashtable.putToHashTable(word, doc);
                        }
                    }
                }
            }
        }
    }
  }
