//! MemoryBackend trait for all storage backends.

use Chottu_core::{ChottuError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, ChottuError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, ChottuError>;
    fn delete(&self, doc_id: &str) -> Result<bool, ChottuError>;
    fn clear(&self) -> Result<(), ChottuError>;
    fn count(&self) -> Result<usize, ChottuError>;
}
