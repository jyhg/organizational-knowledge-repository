from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EvalMetrics(BaseModel):
    faithfulness: float
    answer_relevancy: float
    context_precision: float
    context_recall: float


class EvalRunResult(BaseModel):
    run_id: str
    name: str
    date: str
    total: int
    passed: int
    failed: int
    metrics: EvalMetrics


@router.get("/metrics", response_model=EvalMetrics)
async def get_latest_metrics():
    """Get the latest evaluation metrics."""
    # TODO: query from evaluation results store
    return EvalMetrics(
        faithfulness=0.0,
        answer_relevancy=0.0,
        context_precision=0.0,
        context_recall=0.0,
    )


@router.get("/runs", response_model=list[EvalRunResult])
async def list_eval_runs():
    """List recent evaluation run results."""
    # TODO: query evaluation history
    return []


@router.post("/trigger")
async def trigger_eval_run():
    """Trigger a new evaluation run."""
    # TODO: launch async eval pipeline
    return {"status": "triggered", "run_id": "pending"}
