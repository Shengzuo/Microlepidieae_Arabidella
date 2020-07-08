#=================================#
# Part 1: Getting the matrices from html files
#=================================#

#==============================================================================
# Setting the directories
setwd("/storage/brno1-cerit/home/shengzuo/Arabidella_second/5_repeatome/10_sp_Arabidella") # Directory Repeats
dir_repeats <- getwd()

setwd("./Galaxy9-[RepeatExplorer2_-_Archive_with_HTML_report_from_data_3]/seqclust/clustering/clusters")  # Directory Clusters
oldwd <- getwd()

if(T){
  newdirs <- list.dirs(recursive = FALSE)

  lista_matrices_semellanza <- list()
  lista_matrices_distancia <- list()
  lista_annotations_summary <- list()
  for(i in 1:length(newdirs)){
    setwd(newdirs[i])
    #==============================================================================
    # Getting the lines of tables
    htmlrows <- readLines("index.html")
    if(length(grep("comparative analysis - observed/expected number of edges between species",htmlrows))>0){
      p_cabeceira <- grep("comparative analysis - observed/expected number of edges between species",htmlrows)
      finais_taboas <- grep("</table>",htmlrows)
      final_taboa <- finais_taboas[finais_taboas>p_cabeceira]
      linhas_taboa <- htmlrows[p_cabeceira:final_taboa[1]]
      p_filas <- grep("<tr>",linhas_taboa)
      
      #==============================================================================
      # Getting the head of the table and cleaning
      cabeceira <- linhas_taboa[(p_filas[1]+2):(p_filas[2]-2)]
      cabeceira <- sub("<th>","",cabeceira)
      cabeceira <- sub("</th>","",cabeceira)
      cabeceira <- gsub(" ","",cabeceira)
      
      #==============================================================================
      # Getting the data from O/E matrices and creating similarity matrices
      matriz_semellanza <- c()
      for(j in 2:length(p_filas)){
        fila <- c()
        for(k in 1:length(cabeceira)){
          fila <- c(fila, linhas_taboa[k+1+p_filas[j]])
        }
        matriz_semellanza <- rbind(matriz_semellanza, fila)
      }
      
      #==============================================================================
      # Cleaning the matrices and setting the data as numeric values
      matriz_semellanza <- sub("<td>","",matriz_semellanza)
      matriz_semellanza <- sub("</td>","",matriz_semellanza)
      matriz_semellanza <- gsub(" ","",matriz_semellanza)
      matriz_semellanza <- as.numeric(matriz_semellanza) # This function transforms the matrix into a vector of n elements, 
      # as it is a squared number, it is reorganized with funcion matrix()
      matriz_semellanza <- matrix(matriz_semellanza, ((length(matriz_semellanza))^(1/2)),((length(matriz_semellanza))^(1/2)))
      colnames(matriz_semellanza) <- cabeceira
      rownames(matriz_semellanza) <- cabeceira
      
      #==============================================================================
      # Getting the distance matrix and saving both (distance and similarity) in two lists
      matriz_distancia <- 1/matriz_semellanza
      
      lista_matrices_semellanza[[i]] <- matriz_semellanza
      lista_matrices_distancia[[i]] <- matriz_distancia
    }else{
      cat("\nCluster",i,"tabla ausente en directorio:",newdirs[i],"\n\n")
    }
    
    #--------------------------------------------------------------------------------------
    # Getting a list with the summary of repeat annotations
    v_limpo <- c() # Taking the rows from annotation table
    if(length(grep("similarity based annotation",htmlrows))>0){
      annotations_header <- grep("similarity based annotation",htmlrows)
      annotations <- htmlrows[annotations_header+1]
      annotations <- gsub(" ", "",annotations)
      annotations <- gsub("<td>", "",annotations)
      annotations <- gsub("<br></td>$", "",annotations)
      
      #--------------------------------------------------------------------------------------
      # Splitting the annotation line into rows
      while(grepl("<br>",annotations)){ # If there is noly one row, it jumps
        cadea_limpa <- sub("<br>[[:alnum:]]*:*.*-*/*$","",annotations)
        annotations <- sub(cadea_limpa,"",annotations)
        annotations <- sub("^<br>","",annotations)
        v_limpo <- c(v_limpo,cadea_limpa) # Taking the chail from the last clean row
      }
      annotations <- c(v_limpo,annotations) # Taking  last clean row, if there is only one, it will be taken here
      
      #--------------------------------------------------------------------------------------
      # Generating a data.frame
      if(grepl("^</td>",annotations[1])==FALSE){
        
        percentage <- annotations
        annotations <- gsub("[0-9]+.[0-9]+%","",annotations)
        percentage <- gsub("%[[:alnum:]]*:*.*-*/*$","",percentage)
        percentage <- sub("<b>","",percentage)
        percentage <- as.numeric(percentage)
        annotations_summary <- cbind(annotations,percentage)
        annotations_summary <- as.data.frame(annotations_summary)
      }else{
        annotations_summary <- c("No similarity hits to repeat databases found") # Standard sentence from html files where there are not known annotations.
        cat("Cluster",i,"No similarity hits to repeat databases found\n")
      }
      
    } 
    #--------------------------------------------------------------------------------------
    lista_annotations_summary[[i]] <- annotations_summary
    
    #======================================================================================
    setwd(oldwd)
  }
  
  
  #==============================================================================
  # Naming the elements of lists and cleaning R environment
  n_cluster <- 1:length(lista_matrices_semellanza)
  nome_cluster <- "Cluster"
  nome_elementos_l <- paste(nome_cluster,n_cluster,sep = "_")
  
  names(lista_matrices_semellanza) <- nome_elementos_l
  names(lista_matrices_distancia) <- nome_elementos_l
  names(lista_annotations_summary) <- nome_elementos_l
  
  rm(annotations,annotations_header,annotations_summary,cabeceira,fila,cadea_limpa,finais_taboas,final_taboa,htmlrows,
     i,j,k,linhas_taboa,matriz_distancia,matriz_semellanza,newdirs,oldwd,p_cabeceira,p_filas,percentage,v_limpo,
     n_cluster,nome_cluster,nome_elementos_l)
}


if(T){
  #==============================================================================
  # Cleaning the lists
  lista_annotations_summary_copy <- lista_annotations_summary
  # Removing those clusters with just one species
  print(length(lista_matrices_distancia))
  for(i in length(lista_matrices_distancia):1){
    if(is.null(lista_matrices_distancia[[i]])){
      cat(names(lista_matrices_distancia[i])," no matrix, repeating element only in a taxon.\n")
      lista_matrices_distancia[[i]] <- NULL
      lista_annotations_summary[[i]] <- NULL
    }
  }

  # Removing those clusters with less species than total included in the analysis
  print(length(lista_matrices_distancia))
  for(i in length(lista_matrices_distancia):1){
    for(j in 1:length(lista_matrices_distancia[[i]][,1])){
      if(is.na(lista_matrices_distancia[[i]][j,1])){
        cat(names(lista_matrices_distancia[i])," NAs, the repetitive element is not present all the study taxa.\n")
        lista_matrices_distancia[[i]] <- NULL
        lista_annotations_summary[[i]] <- NULL
        break
      }
    }
  }

  # Removing those matrices showing inf elements (i.e. 0 similarity)
  print(length(lista_matrices_distancia))
  for(i in length(lista_matrices_distancia):1){
    aaa = 0
    for(j in 1:length(lista_matrices_distancia[[i]][,1])){
      for(k in 1:length(lista_matrices_distancia[[i]][1,])){
        if(is.infinite(lista_matrices_distancia[[i]][j,k])){
          aaa = 1
       }
      }
    }
    if(aaa==1){
      cat(names(lista_matrices_distancia[i])," in the similarity matrix there are 0 values that cause the indeterminacy 1/0.\n")
      lista_matrices_distancia[[i]] <- NULL
      lista_annotations_summary[[i]] <- NULL
    }
  }

  # Removing those clusters showing more than 5% of sequences annotated as chloroplast
  print(length(lista_matrices_distancia))
  for(i in length(lista_annotations_summary):1){
    if(is.null(dim(lista_annotations_summary[[i]]))==FALSE){
      j <- length(lista_annotations_summary[[i]][,1])
      while(j>=1){ # A loop for is problematic if the element being read has been removed
        if(grepl("organelle",lista_annotations_summary[[i]][,1][j])){
          if(5<as.numeric(as.character(lista_annotations_summary[[i]][,2][j]))){
            cat(names(lista_annotations_summary[i])," has proportion of organelles elements greater than 5%.\n")            
            lista_matrices_distancia[[i]] <- NULL
            lista_annotations_summary[[i]] <- NULL
            j <- 0
          }
        }
        j <- j-1
      }
    }
  }
  rm(i,j,k)
}

print(length(lista_matrices_distancia))

#================================#
# Part 2: Getting the trees |
#================================#

if(T){
  setwd(dir_repeats)
  dir.create("./00_ape_trees")
  setwd("/storage/brno1-cerit/home/shengzuo/Arabidella_second/5_repeatome/10_sp_Arabidella/00_ape_trees")
  #==============================================================================
  # Install/load "ape" library
  if (!requireNamespace("ape", quietly = TRUE)) {
    install.packages("ape")  
  }
  library(ape)
  
  #==============================================================================
  # Preparing the names of future files
  tree_names <- names(lista_matrices_distancia)
  tree_names <- gsub("Cluster", "tree_CL",tree_names)
  tree_file_names <- paste(tree_names,"nex", sep = ".")
  
  #==============================================================================
  # Running nj() funtion in each matrix and saving the list of trees
  tree_list <- list()
  for(i in 1: length(lista_matrices_distancia)){
    tree <- nj(as.dist(lista_matrices_distancia[[i]]))
    tree_list[[i]] <- tree
  }
  names(tree_list) <- tree_names
  
  #==============================================================================
  # Writing the files for each of the trees
  for(i in 1: length(tree_list)){
    write.nexus(tree_list[[i]], file=tree_file_names[i])
  }
  rm(i)
  
  #==============================================================================
  # Wiriting a general file and visualizing individually 
  write.nexus(tree_list,file="general_tree_list.nex")
  
  general_tree <- read.nexus(file="general_tree_list.nex")
  
  #==============================================================================
  # Writing .tre file
  write.tree(general_tree, file="general_tree_list_newick.tre", append = FALSE,digits = 10, tree.names = FALSE)
  
  #==============================================================================
  # Writing a consensus tree. However, we would recommend using Splitstree to build consensus networks as those presented in MPE paper
  consensus_tree <- consensus(tree_list, p = 0.5, check.labels = TRUE)
  plot(consensus_tree, type="unrooted")
  
}

#---------------------------------------
# Sampling trees, modify as preferred
plot(tree_list[[1]], type="unrooted") # showing the secteted tree changing the index
plot(general_tree, type="unrooted") # showing all the trees, press Enter to skip from one to the next 
plot(consensus_tree, type="unrooted") # showing consensus tree
